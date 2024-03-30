from django import forms
from text_to_speech.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'date_of_birth', 'password')
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Username",
                },
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email",
                },
            ),
            'password': forms.PasswordInput(
                attrs={
                    "placeholder": "Password",
                },
            ),
        }
