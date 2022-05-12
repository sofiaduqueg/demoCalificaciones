from unittest.util import _MAX_LENGTH
from django.db import models

class Transaccion(models.Model):
    sentenciaTransaccion = models.CharField(max_length=100)
    dateTime = models.DateTimeField()
    
    def __str__(self):
        return '{}'.format(self.sentenciaTransaccion)
    
