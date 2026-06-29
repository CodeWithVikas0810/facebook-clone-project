from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignupForm(UserCreationForm):
    """We inherited UserCreationForm class it already knows pass1,pas2
    compare both hash pass and save safely"""

    class Meta:
        """Meta means configuration for the form"""

        model = User  
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )  


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
