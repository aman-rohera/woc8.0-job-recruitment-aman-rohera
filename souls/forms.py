from django import forms
from django.contrib.auth.forms import UserCreationForm
# Ensure both models are imported
from .models import CursedUser, SoulProfile

# ==========================================
# 1. REGISTRATION FORM (Sign Up)
# ==========================================
class SoulRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="Mortal First Name")
    last_name = forms.CharField(label="Mortal Last Name")
    email = forms.EmailField(label="Spirit Signal (Email)")
    phone = forms.CharField(label="Telepathy Number")
    location = forms.CharField(label="Crypt Location")

    class Meta:
        model = CursedUser
        fields = [
            'reincarnation_type', 
            'first_name', 'last_name', 'username', 'email', 
            'phone', 'location', 
            'employer_role', 'organization_name'
        ]

    def __init__(self, *args, **kwargs):
        super(SoulRegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'spooky-input'})

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('reincarnation_type')
        org = cleaned_data.get('organization_name')
        role = cleaned_data.get('employer_role')

        if user_type == 'dungeon_master':
            if not org:
                self.add_error('organization_name', "Dungeon Masters must reveal their Organization!")
            if not role:
                self.add_error('employer_role', "Are you HR or Direct Company?")
        
        return cleaned_data

# ==========================================
# 2. USER UPDATE FORM (Identity: Name, Phone, Org)
# ==========================================
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="Spirit Signal (Email)")
    first_name = forms.CharField(label="Mortal First Name")
    last_name = forms.CharField(label="Mortal Last Name")

    class Meta:
        model = CursedUser
        # ✅ REMOVED 'coven_website' from here
        fields = ['first_name', 'last_name', 'email', 'phone', 'location', 'organization_name']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'spooky-input'})

# ==========================================
# 3. PROFILE FORM (Details: Resume, Website, Bio)
# ==========================================
class SoulProfileForm(forms.ModelForm):
    class Meta:
        model = SoulProfile
        fields = ['resurrection_scroll', 'dark_arts', 'portal_url', 'coven_website', 'coven_description']
        
       
        widgets = {
            'resurrection_scroll': forms.FileInput(), 
        }

    def __init__(self, *args, **kwargs):
        super(SoulProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'spooky-input'})


# ==========================================
# 4. PROFILE COMPLETION FORM (For Social Auth Users)
# ==========================================
class ProfileCompletionForm(forms.ModelForm):
    """Form for completing profile after Google sign-in."""
    username = forms.CharField(
        label="Soul ID (Username)",
        help_text="Choose a unique username"
    )
    
    class Meta:
        model = CursedUser
        fields = ['username', 'reincarnation_type', 'phone', 'location', 'employer_role', 'organization_name']

    def __init__(self, *args, **kwargs):
        super(ProfileCompletionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'spooky-input'})
        # Make phone and location optional for initial completion
        self.fields['phone'].required = False
        self.fields['location'].required = False
        self.fields['employer_role'].required = False
        self.fields['organization_name'].required = False

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Check if username is taken (excluding current user)
        if CursedUser.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This Soul ID is already taken by another spirit!")
        return username

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('reincarnation_type')
        org = cleaned_data.get('organization_name')
        role = cleaned_data.get('employer_role')

        if user_type == 'dungeon_master':
            if not org:
                self.add_error('organization_name', "Dungeon Masters must reveal their Organization!")
            if not role:
                self.add_error('employer_role', "Are you HR or Direct Company?")
        
        return cleaned_data