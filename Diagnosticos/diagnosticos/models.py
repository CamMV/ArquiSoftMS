from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField, ReferenceField, ListField

# Create your models here.
class Diagnostico(Document):
    resultado = StringField(required=True)
    diagnostico = StringField(required=True)
    fecha_diagnostico = DateTimeField(required=True)
    version = StringField(required=True)
    
class IntentoDiagnostico(Document):
    diagnostico = ReferenceField(Diagnostico, required=True)
    fecha_intento = DateTimeField(required=True)
    cambio = StringField(required=True)    