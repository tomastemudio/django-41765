from django.db import models
from django.forms import CharField

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length = 20)
    tipo = models.CharField(max_length = 20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Tipo: {self.tipo}'
