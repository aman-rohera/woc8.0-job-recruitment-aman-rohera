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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        resume = cleaned_data.get('resume')
        use_profile_resume = self.data.get('use_profile_resume')
        # If no resume uploaded and not using profile resume, raise error
        if not resume and not use_profile_resume:
            self.add_error('resume', 'Resume is required to apply.')
        # If user has no profile resume and didn't upload, error
        if not resume and use_profile_resume and self.user:
            try:
                if not hasattr(self.user, 'profile') or not self.user.profile.resurrection_scroll:
                    self.add_error('resume', 'You must upload a resume or add one to your profile.')
            except Exception:
                self.add_error('resume', 'You must upload a resume or add one to your profile.')
        return cleaned_data