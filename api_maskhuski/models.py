from django.db import models
from django.contrib.auth.models import User

# Modelo Billetes:
# Maneja la información y contiene la imagen de cada billete.
class Billetes(models.Model):
    id_billete = models.AutoField(primary_key=True)
    id_nivel = models.IntegerField()
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to='billetes/')

    class Meta:
        db_table = 'billetes'

    def __str__(self):
        return f'Billete {self.id_billete}'

# Modelo Monedas:
# Maneja la información y contiene la imagen de cada moneda.
class Monedas(models.Model):
    id_moneda = models.AutoField(primary_key=True)
    id_nivel = models.IntegerField()
    cantidad = models.IntegerField()    
    imagen = models.ImageField(upload_to='monedas/')

    class Meta:
        db_table = 'monedas'

    def __str__(self):
        return f'Moneda {self.id_moneda}'
    
# Modelo Niveles:
class Niveles(models.Model):
    id_nivel = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tiempo = models.TimeField()

    class Meta:
        db_table = 'niveles'

    def __str__(self):
        return f'Nivel {self.id_nivel} - Usuario: {self.id_usuario.username}'
    
# Modelo Puntaje:
class Puntaje(models.Model):
    id_puntaje = models.AutoField(primary_key=True)
    id_nivel = models.ForeignKey(Niveles, on_delete=models.CASCADE)
    aciertos = models.IntegerField()

    class Meta:
        db_table = 'puntaje_info'

    def __str__(self):
        return f'Puntaje {self.id_puntaje} - Nivel {self.id_nivel.id_nivel}'
    
# Modelo RegistroPuntuacion:
class RegistroPuntuacion(models.Model):
    id_registro_puntuacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_nivel = models.ForeignKey(Niveles, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'registro_puntuacion'

    def __str__(self):
        return f'Registro de Puntuación {self.id_registro_puntuacion} - Usuario {self.id_usuario.username}'

# Modelo Usuario:
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.nombre
