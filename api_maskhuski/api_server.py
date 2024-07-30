#API_SERVER

from .models import Billetes, Monedas, Niveles, Puntaje, RegistroPuntuacion, Usuario
from rest_framework import viewsets, permissions
from .serializers import BilletesSerializer, MonedasSerializer, NivelesSerializer, PuntajeSerializer, RegistroPuntuacionSerializer, UsuarioSerializer


class BilletesViewSet(viewsets.ModelViewSet):
    queryset = Billetes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BilletesSerializer

class MonedasViewSet(viewsets.ModelViewSet):
    queryset = Monedas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MonedasSerializer

class NivelesViewSet(viewsets.ModelViewSet):
    queryset = Niveles.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NivelesSerializer

class PuntajeViewSet(viewsets.ModelViewSet):
    queryset = Puntaje.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PuntajeSerializer

class RegistroPuntuacionViewSet(viewsets.ModelViewSet):
    queryset = RegistroPuntuacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistroPuntuacionSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer
   
