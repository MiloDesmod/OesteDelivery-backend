# locales/admin.py

from django.contrib import admin
from .models import Local, Producto

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    # Quitamos 'esta_abierto' y agregamos el nuevo campo 'imagen'
    list_display = ('nombre', 'dueño', 'direccion', 'imagen')
    # Quitamos el filtro por 'esta_abierto' que no existe
    list_filter = ('dueño',)
    search_fields = ('nombre', 'dueño__email')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """
    Personaliza la vista de los Productos en el panel de administración.
    """
    # Quitamos 'disponible' y agregamos el nuevo campo 'imagen'
    list_display = ('nombre', 'local', 'precio', 'imagen')
    # Quitamos el filtro por 'disponible' que no existe
    list_filter = ('local',)
    search_fields = ('nombre', 'local__nombre')