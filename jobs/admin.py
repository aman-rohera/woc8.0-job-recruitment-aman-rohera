from django.contrib import admin
from .models import JobPost

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    # Columns to show in the list
    list_display = ('title', 'summoner', 'contract_type', 'bounty_gold', 'posted_at')
    
    # Add filters on the right side
    list_filter = ('contract_type', 'posted_at')
    
    # Add a search bar
    search_fields = ('title', 'description', 'summoner__username')