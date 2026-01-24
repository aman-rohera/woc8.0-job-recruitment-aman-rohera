from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CursedUser, SoulProfile

# 1. Custom User Admin
# We use UserAdmin so passwords and permissions work correctly
class CursedUserAdmin(UserAdmin):
    model = CursedUser
    
    # Columns to show in the list view (updated with your NEW field names)
    list_display = ['username', 'email', 'reincarnation_type', 'location', 'organization_name', 'is_staff']
    
    # Filters on the right sidebar
    list_filter = ['reincarnation_type', 'is_staff']

    # Layout for the "Edit User" page
    # We add a custom section for your Spooky fields
    fieldsets = UserAdmin.fieldsets + (
        ('Spooky Identity', {'fields': ('reincarnation_type', 'phone', 'location')}),
        ('Employer Details', {'fields': ('employer_role', 'organization_name')}),
    )
    
    # Layout for the "Add User" page
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('reincarnation_type', 'phone', 'location', 'email')}),
    )

# 2. Soul Profile Admin
# We removed 'crypt_location' because it is now in the User model!
@admin.register(SoulProfile)
class SoulProfileAdmin(admin.ModelAdmin):
    # Only display fields that actually exist in SoulProfile
    list_display = ('user', 'coven_website') 
    search_fields = ('user__username', 'user__email')

# Register the User model with our custom configuration
admin.site.register(CursedUser, CursedUserAdmin)