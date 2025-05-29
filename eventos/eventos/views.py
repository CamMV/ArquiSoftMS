# pylint: disable=no-member

import requests
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Evento
from .serializers import EventoSerializer

# URL del microservicio de pacientes
#TODO: Cambia esta URL por la del microservicio de pacientes 
PACIENTES_SERVICE_URL = 'http://localhost:8001/patients/' 

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        paciente_data = self.get_paciente(instance.paciente_id)
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['paciente'] = paciente_data
        return Response(data)

    def get_paciente(self, paciente_id):
        try:
            response = requests.get(f"{PACIENTES_SERVICE_URL}{paciente_id}")
            if response.status_code == 200:
                return response.json()
            return {"error": "Paciente no encontrado"}
        except requests.exceptions.RequestException:
            return {"error": "Error al conectar con el servicio de pacientes"}
