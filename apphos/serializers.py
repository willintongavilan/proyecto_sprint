from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import paciente

class pacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=paciente
        fields='__all__'