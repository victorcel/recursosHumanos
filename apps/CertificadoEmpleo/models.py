# Create your models here.
from django.db import models


class Empleado(models.Model):
    cedula=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellido)