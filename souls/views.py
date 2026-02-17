from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from .models import SoulProfile, CursedUser
from .forms import (
    SoulProfileForm,
    SoulRegistrationForm,
    UserUpdateForm,
    ProfileCompletionForm
)

# =========================================================
# 1. PUBLIC VIEWS
# =========================================================

def graveyard_welcome(request):
    """
    Home Page (Graveyard Welcome).
    """
    context = {
        'greeting': 'Welcome to the CareerSphere Graveyard',
        'spooky_messages': [
            'Beware of the bugs...',
            'Deadlines are closer than they appear...',
            'Your soul is now bound to Django...'
        ]
    }
    return render(request, 'souls/home.html', context)


def register(request):
    """
    Signup Ritual.
    Creates User + empty SoulProfile.
    """
    if request.method == 'POST':
        form = SoulRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile_complete = True  # Normal signup is complete
            user.save()

            # Create profile safely (ONE profile per user)
            SoulProfile.objects.create(user=user)

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Your soul has been successfully summoned!")
            return redirect('dashboard')
    else:
        form = SoulRegistrationForm()

    return render(request, 'registration/signup.html', {'form': form})


@login_required
def complete_profile(request):
    """
    Complete profile after Google sign-in.
    Asks for username and role.
    """
    # If profile is already complete, redirect to dashboard
    if request.user.profile_complete:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile_complete = True
            user.save()
            
            # Create SoulProfile if not exists
            SoulProfile.objects.get_or_create(user=user)
            
            messages.success(request, "Your spirit identity has been sealed! Welcome to the Graveyard.")
            return redirect('dashboard')
    else:
        form = ProfileCompletionForm(instance=request.user)
    
    return render(request, 'registration/complete_profile.html', {'form': form})


def check_username_available(request):
    """
    AJAX endpoint to check if username is available.
    """
    username = request.GET.get('username', '')
    user_id = request.GET.get('user_id', None)
    
    if username:
        query = CursedUser.objects.filter(username=username)
        if user_id:
            query = query.exclude(pk=user_id)
        
        if query.exists():
            return JsonResponse({'is_taken': True, 'error_message': 'This Soul ID is already taken!'})
        return JsonResponse({'is_taken': False})
    
    return JsonResponse({'is_taken': False})


# =========================================================
# 2. PRIVATE VIEWS
# =========================================================

@login_required
def soul_dashboard(request):
    """
    Profile dashboard (The Crypt).
    """
    # Redirect to complete profile if not done (for Google sign-in users)
    if not request.user.profile_complete:
        return redirect('complete_profile')
    
    profile, _ = SoulProfile.objects.get_or_create(user=request.user)

    context = {
        'profile': profile,
        'user': request.user,
    }
    return render(request, 'souls/dashboard.html', context)


@login_required
def soul_edit(request):
    """
    Edit profile (The Ritual Chamber).
    """
    profile, _ = SoulProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        # Check if user is trying to upload a new resume while one exists
        if profile.resurrection_scroll and 'resurrection_scroll' in request.FILES:
            messages.error(request, "⚠️ You must delete the existing scroll before uploading a new one!")
            return redirect('soul_edit')
        
        p_form = SoulProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your ritual has been sealed (Updated).")
            return redirect('dashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = SoulProfileForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile': profile
    }
    return render(request, 'souls/edit_profile.html', context)


# =========================================================
# 3. DANGER ZONE
# =========================================================

@login_required
def banish_soul_to_void(request):
    """
    Deletes the user account.
    """
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Your soul has been banished to the void.")
        return redirect('home')

    return render(request, 'souls/confirm_banishment.html')


# =========================================================
# 4. AJAX HELPERS
# =========================================================

def check_username_email(request):
    """
    AJAX check for username/email availability.
    """
    username = request.GET.get('username')
    email = request.GET.get('email')

    data = {
        'is_taken': False,
        'error_message': ''
    }

    if username and CursedUser.objects.filter(username__iexact=username).exists():
        data['is_taken'] = True
        data['error_message'] = '⚠️ This Soul ID is already occupied.'

    if email and CursedUser.objects.filter(email__iexact=email).exists():
        data['is_taken'] = True
        data['error_message'] = '⚠️ A soul with this signal already exists.'

    return JsonResponse(data)


# =========================================================
# 5. RESUME DELETE (FIXED & SAFE)
# =========================================================

@login_required
def delete_resume(request):
    """
    Safely deletes the resume scroll.
    """
    profile = request.user.profile

    if profile.resurrection_scroll:
        # Delete file from storage
        profile.resurrection_scroll.delete(save=False)

        # Clear DB field
        profile.resurrection_scroll = None
        profile.save()

        messages.success(request, "The resurrection scroll has been burned.")

    return redirect('soul_edit')
