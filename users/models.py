from django.db import models

# Create your models here.

class DatosUsuario(models.Model):
    cedula = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)