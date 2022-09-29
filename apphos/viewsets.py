from rest_framework import viewsets
from . import models
from . import serializers

class pacienteViewset(viewsets.ModelViewSet):
    queryset=models.paciente.objects.all()
    serializer_class=serializers.pacienteSerializer