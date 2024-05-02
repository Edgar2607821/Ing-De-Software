from django.urls import path
from .views import (index, baseuser, CustomLoginView)

urlpatterns = [
    path('', index, name='index'),
    path('user/', baseuser, name='baseuser'),
    #path('home/', homeuser, name='homeuser'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
