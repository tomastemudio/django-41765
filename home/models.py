from django.db import models

# Create your models here.

# Quiero almacenar esto en la base de datos con el codigo: 'python3 manage.py makemigrations'
# Debo decirle en settings que tengo una nueva app.

class Persona(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateTimeField(null=True)