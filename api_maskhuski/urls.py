#RUTAS

from rest_framework import routers
from .api_server import  BilletesViewSet, MonedasViewSet, NivelesViewSet, PuntajeViewSet, RegistroPuntuacionViewSet, UsuarioViewSet 


from django.urls import path, include
from rest_framework import routers
from .api_server import BilletesViewSet, MonedasViewSet, PuntajeViewSet, RegistroPuntuacionViewSet, UsuarioViewSet

router = routers.DefaultRouter()

router.register(r'api/billetes', BilletesViewSet, basename='billetes')
router.register(r'api/monedas', MonedasViewSet, basename='monedas')
router.register(r'api/niveles', NivelesViewSet, basename='niveles')
router.register(r'api/puntaje', PuntajeViewSet, basename='puntaje')
router.register(r'api/registro_puntuacion', RegistroPuntuacionViewSet, basename='registro_puntuacion')
router.register(r'api/usuario', UsuarioViewSet, basename='usuario')


urlpatterns = router.urls
