from django.db import models
from django.conf import settings

JOB_TYPES = (
    ('full_moon', 'Full Moon (Full Time)'),
    ('half_moon', 'Half Moon (Part Time)'),
    ('eclipse', 'Eclipse (Contract)'),
)

class JobPost(models.Model):
    # Link to the employer (The Dungeon Master)
    summoner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='posted_jobs',
        limit_choices_to={'reincarnation_type': 'dungeon_master'}, # Only employers can post
        verbose_name="Summoner (Employer)"
    )
    
    title = models.CharField(max_length=200, help_text="Role Title (e.g., Head Witch)")
    

    description = models.TextField(verbose_name="Grim Details (Description)")
    haunted_ground = models.CharField(max_length=100, verbose_name="Haunted Ground (Location)")
    
    bounty_gold = models.CharField(
        max_length=100, 
        verbose_name="Bounty (Salary)", 
        help_text="e.g. 500 Gold Coins / Month"
    )
    
    contract_type = models.CharField(
        max_length=20, 
        choices=JOB_TYPES, 
        default='full_moon',
        verbose_name="Moon Phase (Job Type)"
    )
    
    posted_at = models.DateTimeField(auto_now_add=True, verbose_name="Summoned Date")

    def __str__(self):
        return self.title