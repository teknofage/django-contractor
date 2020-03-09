from .models import Profile
from django import forms


class ProfileSetupForm(forms.ModelForm):
    
    
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'zodiac_animal', 'gender']
        
class ProfileUpdateForm(forms.ModelForm):
    
    
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'zodiac_animal', 'gender']