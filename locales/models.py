# locales/models.py
from django.db import models
from usuarios.models import Usuario

class Local(models.Model):
    dueño = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="locales")
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, null=True, blank=True)
    imagen = models.ImageField(upload_to='locales/', null=True, blank=True)

    # --- AÑADIMOS ESTA CLASE META ---
    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locales"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE, related_name="productos")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    # --- AÑADIMOS ESTA CLASE META ---
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre