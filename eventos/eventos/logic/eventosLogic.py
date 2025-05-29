from ..models import Evento


def getEventos():
    eventos = Evento.objects.all()
    return eventos

def createEvento(form):
    if form is None:
        return ()
    else:
        form.save()
        return ()
