# locales/permissions.py

from rest_framework.permissions import BasePermission

class IsDueño(BasePermission):
    """
    Permiso personalizado para permitir solo a los dueños de un local
    ver la información de ese local.
    """
    def has_object_permission(self, request, view, obj):
        # La condición es simple: el dueño del local (obj.dueño)
        # debe ser el mismo que el usuario que hace la request.
        return obj.dueño == request.user
