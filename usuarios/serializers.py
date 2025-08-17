# usuarios/serializers.py
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'email', 'nombre', 'apellido')


# --- ASEGÚRATE DE QUE ESTA CLASE ESTÉ PRESENTE ---
# Este es nuestro serializer de registro personalizado
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return attrs

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            nombre=validated_data.get('nombre', ''),
            apellido=validated_data.get('apellido', '')
        )
        return user