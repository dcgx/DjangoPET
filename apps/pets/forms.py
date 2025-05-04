from django import forms
from .models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
