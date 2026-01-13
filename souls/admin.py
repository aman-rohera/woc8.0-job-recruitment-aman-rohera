from django.contrib import admin
from .models import CursedUser, SoulProfile

@admin.register(CursedUser)
class CursedUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'reincarnation_type', 'is_staff')

@admin.register(SoulProfile)
class SoulProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'crypt_location', 'coven_name')