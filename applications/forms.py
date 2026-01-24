from django import forms
from .models import DarkApplication

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = DarkApplication
        fields = ['cover_scroll', 'resume'] 
        widgets = {
            'cover_scroll': forms.Textarea(attrs={
                'class': 'spooky-input', 
                'rows': 5, 
                'placeholder': 'Incantation: Why should we summon you?'
            }),
        }