# MODELS 

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Billetes(models.Model):
    id_billete = models.AutoField(primary_key=True)
    id_nivel = models.IntegerField()
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to='billetes/')

    def __str__(self):
        return f'Billete {self.id_billete}'

#Modelo monedas:

class Monedas(models.Model):
    id_moneda = models.AutoField(primary_key=True)
    id_nivel = models.IntegerField()
    cantidad = models.IntegerField()    
    imagen = models.ImageField(upload_to='monedas/')

    def __str__(self):
        return f'Moneda {self.id_moneda}'
    

#Modelo niveles:

class Niveles(models.Model):
    id_nivel = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tiempo = models.TimeField()

    def __str__(self):
        return f'Nivel {self.id_nivel} - Usuario: {self.id_usuario.username}'
    
#Modelo puntaje:

class Puntaje(models.Model):
    id_puntaje = models.AutoField(primary_key=True)
    id_nivel = models.ForeignKey(User, on_delete=models.CASCADE)
    aciertos = models.IntegerField()

    def __str__(self):
        return f'Puntaje {self.id_puntaje} - Nivel {self.id_nivel.id_nivel}'
    
#Modelo registro puntuación

class RegistroPuntuacion(models.Model):
    id_registro_puntuacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_nivel = models.ForeignKey(Niveles, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Registro de Puntuación {self.id_registro_puntuacion} - Usuario {self.id_usuario.username}'

#Modelo usuario:

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
