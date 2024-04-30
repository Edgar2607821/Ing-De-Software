from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth.views import LoginView
# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'encuestas/login.html'  # Reemplaza 'tu_template_de_login.html' con el nombre de tu plantilla
    form_class = LoginForm