from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'country']

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['resume']
        widgets = {
            'resume': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }