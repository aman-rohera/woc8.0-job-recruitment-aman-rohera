from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.base import ContentFile

from .models import DarkApplication
from .forms import ApplicationForm
from jobs.models import JobPost


@login_required
def apply_to_job(request, job_id):
    """Seeker applies to a job."""
    job = get_object_or_404(JobPost, pk=job_id)
    
    if request.user.reincarnation_type != 'specter':
        messages.error(request, "Only Specters (Job Seekers) can apply!")
        return redirect('job_detail', pk=job_id)
    
    # Check if already applied
    if DarkApplication.objects.filter(job=job, seeker=request.user).exists():
        messages.warning(request, "You've already applied to this dark opportunity!")
        return redirect('job_detail', pk=job_id)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.seeker = request.user
            
            # If no new resume uploaded and user wants to use profile resume
            if not request.FILES.get('resume') and request.POST.get('use_profile_resume'):
                try:
                    profile = request.user.profile
                    if profile.resurrection_scroll:
                        # Just reference the same file path (don't copy)
                        application.resume = profile.resurrection_scroll.name
                except Exception as e:
                    pass  # If copy fails, just continue without resume
            
            application.save()
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('job_list')
        else:
            messages.error(request, "Please fill in all required fields.")
    else:
        form = ApplicationForm(user=request.user)
    
    return render(request, 'applications/apply.html', {'form': form, 'job': job})


@login_required
def my_applications(request):
    """Seeker views all their applications."""
    applications = DarkApplication.objects.filter(seeker=request.user).order_by('-applied_at')
    return render(request, 'applications/my_applications.html', {'applications': applications})


@login_required
def withdraw_application(request, pk):
    """Seeker withdraws their application (only if still pending)."""
    application = get_object_or_404(DarkApplication, pk=pk, seeker=request.user)
    
    # Only allow withdrawal if status is still pending (purgatory)
    if application.doom_status != 'purgatory':
        messages.error(request, "You can only withdraw applications that are still in Purgatory (Pending)!")
        return redirect('my_applications')
    
    if request.method == 'POST':
        application.delete()
        messages.success(request, "Your application has been withdrawn from the void!")
        return redirect('my_applications')
    
    return render(request, 'applications/withdraw_confirm.html', {'application': application})


@login_required
def job_applications(request, job_id):
    """Employer views all applications for their job."""
    job = get_object_or_404(JobPost, pk=job_id, summoner=request.user)
    applications = DarkApplication.objects.filter(job=job).order_by('-applied_at')
    return render(request, 'applications/job_applications.html', {'job': job, 'applications': applications})


@login_required
def application_detail(request, pk):
    """View a single application (for employer)."""
    application = get_object_or_404(DarkApplication, pk=pk)
    
    # Only the job owner or applicant can view
    if application.job.summoner != request.user and application.seeker != request.user:
        messages.error(request, "You don't have permission to view this application!")
        return redirect('dashboard')
    
    return render(request, 'applications/application_detail.html', {'application': application})


@login_required
def update_status(request, pk):
    """Employer updates application status."""
    application = get_object_or_404(DarkApplication, pk=pk)
    
    if application.job.summoner != request.user:
        messages.error(request, "Only the job owner can update application status!")
        return redirect('dashboard')
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['purgatory', 'ascended', 'banished']:
            application.doom_status = new_status
            application.save()
            messages.success(request, f"Application fate updated to {application.get_doom_status_display()}!")
    
    return redirect('application_detail', pk=pk)
