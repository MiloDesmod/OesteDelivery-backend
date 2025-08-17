# locales/urls.py

from django.urls import path
from .views import ListaDeLocales, DetalleDeLocal

urlpatterns = [
    # La ruta para la lista de locales
    path('locales/', ListaDeLocales.as_view(), name='lista-locales'),
    
    # La nueva ruta para el detalle, que acepta un ID numérico
    path('locales/<int:pk>/', DetalleDeLocal.as_view(), name='detalle-local'),
]