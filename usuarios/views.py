# usuarios/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Usuario
from .serializers import UserRegistrationSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    permission_classes = (AllowAny,) # Cualquiera puede registrarse
    serializer_class = UserRegistrationSerializer