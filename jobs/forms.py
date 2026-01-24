from django import forms
from .models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        # MUST match the variable names in your models.py
        fields = ['title', 'description', 'haunted_ground', 'bounty_gold', 'contract_type']
        
    def __init__(self, *args, **kwargs):
        super(JobPostForm, self).__init__(*args, **kwargs)
        # Apply spooky styling
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'spooky-input'})