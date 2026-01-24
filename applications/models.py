from django.db import models
from django.conf import settings
from jobs.models import JobPost

STATUS_CHOICES = (
    ('purgatory', 'In Purgatory (Pending)'),
    ('ascended', 'Ascended (Accepted)'),
    ('banished', 'Banished (Rejected)'),
)

class DarkApplication(models.Model):
    # The Job being applied for
    job = models.ForeignKey(
        JobPost, 
        on_delete=models.CASCADE, 
        related_name='applications'
    )
    
    # The Job Seeker (Specter)
    seeker = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='applications'
    )
    
    # other content
    cover_scroll = models.TextField(
        verbose_name="Incantation (Cover Letter)", 
        help_text="Why should we summon you?"
    )
    
    # Resume for this application
    resume = models.FileField(
        upload_to='application_resumes/',
        blank=True,
        null=True,
        verbose_name="Resume"
    )
    
    doom_status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='purgatory',
        verbose_name="Fate (Status)"
    )
    
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent applying to the same job twice
        unique_together = ('job', 'seeker')

    def __str__(self):
        return f"{self.seeker} -> {self.job}"