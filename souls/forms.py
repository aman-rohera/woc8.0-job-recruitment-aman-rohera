from django import forms
from django.core.exceptions import ValidationError
from .models import CursedUser, SoulProfile

class SoulRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = CursedUser
        fields = ['username', 'email', 'password', 'reincarnation_type']

class SoulProfileForm(forms.ModelForm):
    class Meta:
        model = SoulProfile
        fields = ['crypt_location', 'telepathy_frequency', 'resurrection_scroll', 
                  'dark_arts', 'portal_url', 'coven_name', 'coven_description']

    # Custom Validation 
    def clean_resurrection_scroll(self):
        scroll = self.cleaned_data.get('resurrection_scroll')
        if scroll:
            if not scroll.name.endswith('.pdf'):
                raise ValidationError("Only ancient scrolls (.pdf) are accepted in the afterlife!")
        return scroll