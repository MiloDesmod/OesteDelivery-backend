# ordenes/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Orden
from .serializers import (
    OrdenParaEscribirSerializer, 
    OrdenParaLeerSerializer, 
    ActualizarEstadoOrdenSerializer
)

class CrearOrden(generics.CreateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenParaEscribirSerializer
    permission_classes = [IsAuthenticated]

    # La vista ahora solo se encarga de pasar el usuario al serializer.
    # Toda la lógica compleja de creación ahora vive en el serializer.
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class HistorialDeOrdenes(generics.ListAPIView):
    serializer_class = OrdenParaLeerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Orden.objects.filter(usuario=self.request.user)

# Dejamos las otras vistas como estaban, ya que las usaremos para el panel del local.
class ListaDeOrdenesLocal(generics.ListAPIView):
    # ... (código existente)
    pass

class DetalleDeOrdenLocal(generics.RetrieveUpdateAPIView):
    # ... (código existente)
    pass