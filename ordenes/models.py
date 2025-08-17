# ordenes/models.py

from django.db import models
from usuarios.models import Usuario
from locales.models import Local, Producto

class Orden(models.Model):
    """
    Representa un pedido realizado por un usuario a un local.
    """
    ESTADO_CHOICES = [
        ('RECIBIDO', 'Recibido'),
        ('EN_PREPARACION', 'En Preparación'),
        ('EN_CAMINO', 'En Camino'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    ]

    # --- Relaciones Clave ---
    # --- LÍNEA CORREGIDA Y RESTAURADA ---
    # Volvemos a hacer que el campo 'usuario' sea obligatorio y que las órdenes se borren si se borra el usuario.
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="ordenes")
    
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True, related_name="ordenes")
    productos = models.ManyToManyField(Producto, through='ItemDeOrden')

    # --- Información del Pedido ---
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='RECIBIDO')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    direccion_entrega = models.CharField(max_length=255)
    notas = models.TextField(blank=True, null=True, verbose_name="Notas Adicionales")

    # --- Timestamps ---
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        # --- LÍNEA SIMPLIFICADA ---
        # Como el usuario ya no puede ser nulo, quitamos la comprobación extra.
        return f"Orden #{self.id} - {self.usuario.email}"

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Órdenes"
        ordering = ['-fecha_creacion']

class ItemDeOrden(models.Model):
    """
    Modelo intermedio para la relación ManyToMany entre Orden y Producto.
    Nos permite guardar la cantidad de cada producto en una orden.
    """
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en Orden #{self.orden.id}"