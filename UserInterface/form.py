from typing import Text
import django.forms as forms
from Models.models import RegisterList

class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterList
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control', 'autocomplete' : 'off'}),
            'program': forms.TextInput(attrs={'placeholder': 'Program', 'class': 'form-control'}),
            'level': forms.TextInput(attrs={'placeholder': 'Level', 'class': 'form-control'}),
            'facebook_link': forms.TextInput(attrs={'placeholder': 'FB Link ', 'class': 'form-control', 'autocomplete': 'off    '}),
            
        }
        fields = ['name', 'program', 'level', 'facebook_link']