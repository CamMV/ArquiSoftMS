# pylint: disable=no-member

import requests
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Evento
from hospital.settings import PATH_PACIENTES
from .serializers import EventoSerializer

# URL del microservicio de pacientes
#TODO: Cambia esta URL por la del microservicio de pacientes 

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def list(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            eventos = self.get_queryset()
            return Response(
                {'eventos': eventos}, 
                template_name='Evento/eventos.html'
            )
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        paciente_data = self.get_paciente(instance.paciente_id)
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['paciente'] = paciente_data
        return Response(data)

    def get_paciente(self, paciente_id):
        try:
            response = requests.get(f"{PATH_PACIENTES}{paciente_id}")
            if response.status_code == 200:
                return response.json()
            return {"error": "Paciente no encontrado"}
        except requests.exceptions.RequestException:
            return {"error": "Error al conectar con el servicio de pacientes"}
