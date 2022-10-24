from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ExtensionUsuario(models.Model):
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  ## ForeignKey es un campo donde el modelo por parte de la foreignkey esta relacionado a un dato que yo le pase.
    user = models.OneToOneField(User, on_delete=models.CASCADE)  ## El OneToOneField nos permite relacionar algo del model al user.