from django.contrib import admin
from .models import DarkApplication

@admin.register(DarkApplication)
class DarkApplicationAdmin(admin.ModelAdmin):
    # Columns to show
    list_display = ('seeker', 'job', 'doom_status', 'applied_at')
    
    # Filters for status (e.g., show me all "Pending/Purgatory" apps)
    list_filter = ('doom_status', 'applied_at')
    
    # Search by applicant name or job title
    search_fields = ('seeker__username', 'job__title')