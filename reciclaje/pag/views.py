from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth.views import LoginView
from .models import Dispositivo, TipoDisp, Marca, Modelo
from django.http import JsonResponse
import json

def index(request): 
    return render(request, 'pag/index.html')

def Servicios(request):
    return render(request, 'pag/Servicios.html')

def Beneficios(request):
    return render(request, 'pag/Beneficios.html')

def baseuser(request):
    return render(request, 'pag/baseuser.html')


class CustomLoginView(LoginView):
    template_name = 'pag/login.html'
    form_class = LoginForm



def cata(request):
    data = {
        "dispositivos": dispositivos(request),
        "tipos": TipoDisp.objects.all(),  # Agrega esta línea para pasar los tipos a la plantilla
    }
    return render(request, 'pag/catalogo.html', data)


def dispositivos(request):
    return Dispositivo.objects.all().order_by('nombre')

def filtrar_tipos(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            dispositivo_id = data.get('dispositivo_id')
            data_bd = list(TipoDisp.objects.filter(dispositivo_id=dispositivo_id).values())

            return JsonResponse({'status': 200, 'data': data_bd})
        else:
            return JsonResponse({'error': 'Método no permitido'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def filtrar_marcas(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            tipo_id = data.get('tipo_id')
            data_bd = list(Marca.objects.filter(tipo_id=tipo_id).values())

            return JsonResponse({'status': 200, 'data': data_bd})
        else:
            return JsonResponse({'error': 'Método no permitido'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def filtrar_modelos(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            marca_id = data.get('marca_id')
            data_bd = list(Modelo.objects.filter(marca_id=marca_id).values())

            return JsonResponse({'status': 200, 'data': data_bd})
        else:
            return JsonResponse({'error': 'Método no permitido'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
