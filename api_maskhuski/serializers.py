#SERIALIZERS


from rest_framework import serializers
from .models import Billetes, Monedas, Niveles, Puntaje, RegistroPuntuacion, Usuario

class BilletesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billetes
        fields = '__all__'

class MonedasSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Monedas
        fields = '__all__'
    
class NivelesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveles
        fields = '__all__'

class PuntajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puntaje
        fields = '__all__'

class RegistroPuntuacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPuntuacion
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'