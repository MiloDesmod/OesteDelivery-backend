# locales/views.py

from rest_framework import generics
from .models import Local
from .serializers import LocalSerializer, DetalleDeLocalSerializer

class ListaDeLocales(generics.ListAPIView):
    serializer_class = LocalSerializer
    
    def get_queryset(self):
        """
        Este método ahora revisa si hay un parámetro 'search' en la URL.
        Si existe, filtra los locales cuyo nombre contenga el texto buscado.
        Si no existe, devuelve todos los locales como antes.
        """
        # Obtenemos todos los locales para empezar
        queryset = Local.objects.all()
        
        # Buscamos el parámetro 'search' en la solicitud
        termino_busqueda = self.request.query_params.get('search', None)
        
        if termino_busqueda is not None:
            # Si hay un término de búsqueda, filtramos el queryset.
            # '__icontains' significa que la búsqueda no distingue mayúsculas/minúsculas.
            queryset = queryset.filter(nombre__icontains=termino_busqueda)
            
        return queryset


class DetalleDeLocal(generics.RetrieveAPIView):
    queryset = Local.objects.all()
    serializer_class = DetalleDeLocalSerializer