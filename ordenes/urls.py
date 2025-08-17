# ordenes/urls.py

from django.urls import path
#from .views import CrearOrden
from .views import CrearOrden, HistorialDeOrdenes, ListaDeOrdenesLocal, DetalleDeOrdenLocal

urlpatterns = [
    # La URL para crear la orden será, por ejemplo, /api/ordenes/crear/
    path('ordenes/crear/', CrearOrden.as_view(), name='crear-orden'),

    # La nueva URL para ver el historial
    path('ordenes/', HistorialDeOrdenes.as_view(), name='historial-ordenes'),

    # Nueva URL para que el dueño vea las órdenes de su local
    path('locales/<int:local_id>/ordenes/', ListaDeOrdenesLocal.as_view(), name='ordenes-local'),
    
    # Nueva URL para ver/modificar UNA orden específica (por su ID)
    path('ordenes/<int:pk>/', DetalleDeOrdenLocal.as_view(), name='detalle-orden-local'),
    
    path('ordenes/historial/', HistorialDeOrdenes.as_view(), name='historial-ordenes'),



]
