from django.db import models
from django.contrib.auth.models import AbstractUser

# ==========================================
# 1. THE USER (Login & Role)
# ==========================================

# Choices for the Role
TYPE_CHOICES = (
    ('specter', 'Wandering Specter (Job Seeker)'),
    ('dungeon_master', 'Dungeon Master (Employer)'),
)

class CursedUser(AbstractUser):
    """
    The Login Account.
    We ask for the ROLE here so we know if they are a Seeker or Employer immediately.
    """
    reincarnation_type = models.CharField(
        max_length=20, 
        choices=TYPE_CHOICES, 
        default='specter',
        verbose_name="Reincarnation Type (Role)",
        help_text="Are you seeking a haunt (Job Seeker) or do you own the dungeon (Employer)?"
    )

    # We can add strict validation here later if needed
    def is_employer(self):
        return self.reincarnation_type == 'dungeon_master'

# ==========================================
# 2. THE PROFILE (Extra Details)
# ==========================================

class SoulProfile(models.Model):
    """
    The Profile Model linked via OneToOne to CursedUser.
    This holds the detailed CV or Company Info.
    """
    user = models.OneToOneField(CursedUser, on_delete=models.CASCADE, related_name='profile')
    
    # --- BASIC IDENTITY ---
    mortal_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Mortal Name (Full Name)",
        help_text="The name you use in the living world."
    )
    
    crypt_location = models.CharField(
        max_length=255, 
        blank=True, 
        verbose_name="Crypt Location (Address/City)", 
        help_text="Where are you currently based?"
    )
    
    telepathy_frequency = models.CharField(
        max_length=15, 
        blank=True, 
        verbose_name="Telepathy Frequency (Phone Number)", 
        help_text="Contact number"
    )

    # --- JOB SEEKER SPECIFIC FIELDS ---
    resurrection_scroll = models.FileField(
        upload_to='scrolls/', 
        blank=True, 
        null=True, 
        verbose_name="Resurrection Scroll (Resume)", 
        help_text="Upload your CV (PDF only)"
    )
    
    dark_arts = models.TextField(
        blank=True, 
        verbose_name="Dark Arts (Skills)", 
        help_text="List your skills (e.g., Python, Django, Spellcasting)"
    )
    
    years_of_decay = models.PositiveIntegerField(
        default=0,
        verbose_name="Years of Decay (Experience)",
        help_text="Years of professional experience"
    )
    
    portal_url = models.URLField(
        blank=True, 
        verbose_name="Portal URL (Portfolio)", 
        help_text="Link to your portfolio or LinkedIn"
    )
    
    # --- EMPLOYER SPECIFIC FIELDS ---
    coven_name = models.CharField(
        max_length=100, 
        blank=True, 
        verbose_name="Coven Name (Company Name)", 
        help_text="Name of your organization"
    )
    
    coven_website = models.URLField(
        blank=True,
        verbose_name="Coven Website (Company Site)"
    )
    
    coven_description = models.TextField(
        blank=True,
        verbose_name="Coven Description (Company Description)",
        help_text="Describe your company culture and mission."
    )

    def __str__(self):
        # Shows "Profile of [Name]" in the Admin Panel
        return f"Profile of {self.mortal_name} ({self.user.username})"