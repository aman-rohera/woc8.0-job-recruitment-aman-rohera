from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. THE CURSED USER (Login & Core Identity)

class CursedUser(AbstractUser):
    TYPE_CHOICES = (
        ('specter', 'Wandering Specter (Job Seeker)'),
        ('dungeon_master', 'Dungeon Master (Employer)'),
    )
    
    EMPLOYER_TYPE_CHOICES = (
        ('hr', 'HR Necromancer (HR Rep)'),
        ('company', 'Coven Leader (Direct Company)'),
    )

    # 1. Role
    reincarnation_type = models.CharField(
        max_length=20, 
        choices=TYPE_CHOICES, 
        default='specter',
        verbose_name="Reincarnation Form (User Role)"
    )

    # 2. Universal Fields
    phone = models.CharField(max_length=15, verbose_name="Telepathy Freq (Phone Number)")
    location = models.CharField(max_length=100, verbose_name="Haunted Ground (Location)")

    # 3. Employer Specific Fields
    employer_role = models.CharField(
        max_length=20, 
        choices=EMPLOYER_TYPE_CHOICES, 
        blank=True, 
        null=True,
        verbose_name="Master Rank (Employer Type)"
    )
    organization_name = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name="Coven Name (Organization)"
    )

    def is_employer(self):
        return self.reincarnation_type == 'dungeon_master'


class SoulProfile(models.Model):
    user = models.OneToOneField(CursedUser, on_delete=models.CASCADE, related_name='profile')
    
    # --- JOB SEEKER EXTRAS ---
    resurrection_scroll = models.FileField(
        upload_to='scrolls/', 
        blank=True, null=True, 
        verbose_name="Resurrection Scroll (Resume PDF)"
    )
    dark_arts = models.TextField(
        blank=True, 
        verbose_name="Dark Arts (Skills & Experience)"
    )
    portal_url = models.URLField(
        blank=True, 
        verbose_name="Summoning Portal (Portfolio Link)"
    )
    
    # --- EMPLOYER EXTRAS ---
    coven_website = models.URLField(
        blank=True, 
        verbose_name="Coven Web (Company Site)"
    )
    coven_description = models.TextField(
        blank=True, 
        verbose_name="Coven Tales (Company Description)"
    )

    def __str__(self):
        return f"Profile of {self.user.username}"