# ordenes/serializers.py

from rest_framework import serializers
from django.db import transaction  # Importamos transaction para asegurar la integridad
from .models import Orden, ItemDeOrden, Producto
from locales.serializers import ProductoSerializer, LocalSimpleSerializer

class ItemDeOrdenParaLeerSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    class Meta:
        model = ItemDeOrden
        fields = ['cantidad', 'producto']

class OrdenParaLeerSerializer(serializers.ModelSerializer):
    items = ItemDeOrdenParaLeerSerializer(source='itemdeorden_set', many=True, read_only=True)
    local = LocalSimpleSerializer(read_only=True)
    class Meta:
        model = Orden
        fields = ['id', 'local', 'estado', 'total', 'direccion_entrega', 'fecha_creacion', 'items']

# --- SERIALIZER DE ESCRITURA CON LA LÓGICA CORREGIDA ---
class OrdenParaEscribirSerializer(serializers.ModelSerializer):
    items = serializers.ListField(child=serializers.DictField(), write_only=True)

    class Meta:
        model = Orden
        # Le decimos al serializer que campos va a recibir. 'total' y 'local' se calcularán, no se recibirán.
        fields = ['direccion_entrega', 'notas', 'items']

    def create(self, validated_data):
        # Sacamos la lista de items de los datos validados
        items_data = validated_data.pop('items')
        
        # Usamos una transacción para que si algo falla, toda la operación se deshaga.
        with transaction.atomic():
            # 1. Calculamos el total y obtenemos el local
            total_orden = 0
            local_de_la_orden = None
            
            for item_data in items_data:
                producto_id = item_data['producto']
                cantidad = item_data['cantidad']
                producto = Producto.objects.get(pk=producto_id)
                
                total_orden += producto.precio * cantidad
                if not local_de_la_orden:
                    local_de_la_orden = producto.local

            # 2. Creamos la Orden principal con los datos calculados
            # El 'usuario' lo pasaremos desde la vista
            orden = Orden.objects.create(
                total=total_orden,
                local=local_de_la_orden,
                **validated_data
            )

            # 3. Creamos cada ItemDeOrden asociado a la Orden principal
            for item_data in items_data:
                ItemDeOrden.objects.create(
                    orden=orden,
                    producto_id=item_data['producto'],
                    cantidad=item_data['cantidad']
                )
        
        return orden

class ActualizarEstadoOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = ['estado']