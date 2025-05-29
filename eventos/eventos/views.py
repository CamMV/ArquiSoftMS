# pylint: disable=no-member

import requests
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Evento
from hospital.settings import PATH_PACIENTES
from .serializers import EventoSerializer
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect

# URL del microservicio de pacientes

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
    
    @action(detail=False, methods=['get'], renderer_classes=[TemplateHTMLRenderer])
    def nuevo(self, request):
        # le pasamos un serializer vacío al template
        return Response(
            {'serializer': EventoSerializer()},
            template_name='Evento/eventoCreate.html'
        )

    # ——— creación (POST) ———
    def create(self, request, *args, **kwargs):
        # si viene de HTML, procesamos el form
        if request.accepted_renderer.format == 'html':
            serializer = EventoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                # una vez creado, redirigimos al listado
                return redirect('evento-list')
            # si hay errores, re-renderizamos el form con ellos
            return Response(
                {'serializer': serializer},
                template_name='Evento/eventoCreate.html',
                status=status.HTTP_400_BAD_REQUEST
            )
        # para JSON delegamos al comportamiento por defecto
        return super().create(request, *args, **kwargs)
    
    def get_paciente(self, paciente_id):
        try:
            response = requests.get(f"{PATH_PACIENTES}{paciente_id}")
            if response.status_code == 200:
                return response.json()
            return {"error": "Paciente no encontrado"}
        except requests.exceptions.RequestException:
            return {"error": "Error al conectar con el servicio de pacientes"}
