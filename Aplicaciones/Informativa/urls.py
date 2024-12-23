#importacion de path urls de python
from django.urls import path
#importar todas las vistas que hay dentro de la app INFORMATIVA

from . import views

#CREAR ARREGLO DE URLS

urlpatterns = [
    path('',views.home,name='home')
]