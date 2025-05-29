# forms.py
from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['paciente_id', 'nombre', 'fecha', 'descripcion']
