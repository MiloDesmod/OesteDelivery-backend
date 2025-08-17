# usuarios/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    """
    Configuración personalizada para el modelo Usuario en el panel de administrador.
    """
    # Los campos que se mostrarán en la lista de usuarios
    list_display = ('email', 'nombre', 'apellido', 'is_staff', 'is_active')
    # Los campos por los que se puede ordenar
    ordering = ('email',)
    # Los campos que no se pueden editar directamente en el formulario de cambio
    # --- LÍNEA CORREGIDA ---
    readonly_fields = ('date_joined',) 

    # Sobrescribimos los fieldsets para adaptarlos a nuestro modelo sin 'username'
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('nombre', 'apellido')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(Usuario, UsuarioAdmin)