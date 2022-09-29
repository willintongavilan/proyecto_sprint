from unittest.util import _MAX_LENGTH
from django.db import models

class paciente(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=(30))
    direccion=models.CharField(max_length=(30))
