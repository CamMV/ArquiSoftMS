from rest_framework import serializers
from . import models


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'paciente', 'diagnostico', 'tipo', 'descripcion', 'fecha',)
        model = models.Evento