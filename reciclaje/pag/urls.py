from django.urls import path
from .views import (index, baseuser, CustomLoginView, filtrar_marcas, filtrar_modelos, filtrar_tipos,cata, Servicios, Beneficios)

urlpatterns = [
    path('', index, name='index'),
    path('servicios/', Servicios, name='servicios'),
    path('beneficios/', Beneficios, name='beneficios'),
    path('user/', baseuser, name='baseuser'),
    #path('home/', homeuser, name='homeuser'),
    path('login/', CustomLoginView.as_view(), name='login'),\
    path('catalogo/', cata, name='catalogo'),
    path('filtrar-tipos/', filtrar_tipos, name='filtrar_tipos'),
    path('filtrar-marcas/', filtrar_marcas, name='filtrar_marcas'),
    path('filtrar-modelos/', filtrar_modelos, name='filtrar_modelos'),
    
]
