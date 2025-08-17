# locales/serializers.py

from rest_framework import serializers
from .models import Producto, Local

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class LocalSerializer(serializers.ModelSerializer):
    # Le decimos que use el ProductoSerializer para mostrar la lista completa de productos
    productos = ProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Local
        fields = ['id', 'nombre', 'direccion', 'logo', 'productos']

class LocalSimpleSerializer(serializers.ModelSerializer):
    # Este es una versión más simple, solo para mostrar en la lista de órdenes
    class Meta:
        model = Local
        fields = ['id', 'nombre', 'logo']

# Este lo necesitará tu vista de DetalleDeLocal
class DetalleDeLocalSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)
    class Meta:
        model = Local
        fields = ['id', 'nombre', 'direccion', 'logo', 'productos']