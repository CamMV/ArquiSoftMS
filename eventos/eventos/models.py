from django.db import models
from django.utils import timezone

# Create your models here.
class Evento(models.Model):
    paciente_id = models.IntegerField()
    tipo = models.CharField(max_length=50, choices=[
        ('MUESTRA_DE_SANGRE', 'Muestra de sangre'),
        ('PRESCRIPCION_DE_MEDICAMENTO', 'Prescripcion de medicamento'),
        ('CONSULTA_MEDICA', 'Consulta medica'),
        ('EXAMEN_MEDICO', 'Examen medico'),
        ('CIRUGIA', 'Cirugia'),
        ('CITA_MEDICA', 'Cita medica'),
    ])
    descripcion = models.CharField(max_length=50)
    fecha = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"Paciente_id: {self.paciente_id}, Evento: {self.tipo}, Descripción: {self.descripcion}, Fecha: {self.fecha}"
