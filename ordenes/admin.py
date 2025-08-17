# ordenes/admin.py

from django.contrib import admin
from .models import Orden, ItemDeOrden

class ItemDeOrdenInline(admin.TabularInline):
    """
    Permite ver y editar los items del pedido directamente
    dentro de la vista de la Orden.
    """
    model = ItemDeOrden
    extra = 1  # Muestra 1 campo extra para añadir un item.

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    """
    Personaliza la vista de las Órdenes en el panel de administración.
    """
    list_display = ('id', 'usuario', 'local', 'estado', 'total', 'fecha_creacion')
    list_filter = ('estado', 'fecha_creacion', 'local')
    search_fields = ('id', 'usuario__email', 'local__nombre')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion', 'total')

    # Esta es la parte avanzada: incrusta los items dentro de la orden.
    inlines = [ItemDeOrdenInline]
