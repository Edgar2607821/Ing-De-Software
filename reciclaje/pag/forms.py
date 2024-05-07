from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import Dispositivo, TipoDisp, Marca, Modelo

class CatalogoForm(forms.Form):
    dispositivo = forms.ModelChoiceField(queryset=Dispositivo.objects.all())
    tipo = forms.ModelChoiceField(queryset=TipoDisp.objects.none())  # Inicialmente vacío
    marca = forms.ModelChoiceField(queryset=Marca.objects.none())  # Inicialmente vacío
    modelo = forms.ModelChoiceField(queryset=Modelo.objects.none())  # Inicialmente vacío


class LoginForm(AuthenticationForm):
    # Puedes personalizar el formulario si es necesario
    pass