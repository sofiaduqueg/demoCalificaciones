from unittest.util import _MAX_LENGTH
from django.db import models

class Vivienda(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    parqueadero = models.BooleanField()
    pagoPorSemestre = models.BooleanField()
    distanciaAlaUniversidad = models.IntegerField()
    def __str__(self):
        return '{}'.format(self.nombre)

class Transporte(models.Model):
    vivienda = models.ForeignKey(Vivienda, related_name = "transportes", on_delete=models.CASCADE)
    idDeVivienda = models.IntegerField()
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    
    def __str__(self):
        return '{}'.format(self.nombre)


class Consulta(models.Model):
    precioMaximo = models.FloatField()
    parqueadero = models.BooleanField()
    distanciaAlaUniversidad = models.IntegerField()
    
