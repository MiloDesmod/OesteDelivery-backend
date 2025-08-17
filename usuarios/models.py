# usuarios/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UsuarioManager(BaseUserManager):
    """
    Manager personalizado para nuestro modelo de Usuario,
    donde el email es el identificador único en lugar del username.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Crea y guarda un Usuario con el email y contraseña dados.
        """
        if not email:
            raise ValueError('El campo Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Crea y guarda un Superusuario con el email y contraseña dados.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de Usuario personalizado que usa email como username.
    """
    email = models.EmailField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255, blank=True)
    apellido = models.CharField(max_length=255, blank=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # Le decimos a Django que vamos a usar nuestro Manager personalizado
    objects = UsuarioManager()

    # Le decimos a Django que el campo 'email' será el usado para el login
    USERNAME_FIELD = 'email'
    # Django no pedirá ningún campo extra al crear un superusuario
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email