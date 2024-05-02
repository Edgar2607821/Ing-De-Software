from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth.views import LoginView

def index(request):
    return render(request, 'pag/index.html')

def baseuser(request):
    return render(request, 'pag/baseuser.html')


class CustomLoginView(LoginView):
    template_name = 'pag/login.html'
    form_class = LoginForm

#@login_required
#def homeuser(request):
#    # Obtén el nombre de usuario del objeto request.user'
#    actualizar_grupos_info(request)
#    nombre_usuario = request.user.username
#
#    # Pasa el nombre de usuario a la plantilla
#    return render(request, 'encuestas/home.html', {'nombre_usuario': nombre_usuario})
#