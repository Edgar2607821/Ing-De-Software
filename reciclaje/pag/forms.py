from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm


class LoginForm(AuthenticationForm):
    # Puedes personalizar el formulario si es necesario
    pass