import json
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Diagnostico, IntentoDiagnostico
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from mongoengine.errors import DoesNotExist

@require_http_methods(["GET"])
def diagnosticos_list(request):
    diagnosticos = Diagnostico.objects.all()
    
    return render(request,'Diagnostico/diagnosticos.html',{
        "diagnosticos": diagnosticos
    })

@require_http_methods(["GET"])
def diagnostico_detail(request, diagnostico_id):
    try:
        diagnostico = Diagnostico.objects.get(id=diagnostico_id)
    except DoesNotExist:
        raise Http404("Diagnostico not found")
    return render(request, 'Diagnostico/diagnostico_detail.html', {
        "diagnostico": diagnostico
    })

@csrf_exempt
@require_http_methods(["GET", "POST"])
def diagnostico_create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        diagnostico = Diagnostico(
            resultado=data.get('resultado'),
            diagnostico=data.get('diagnostico'),
            fecha_diagnostico=data.get('fecha_diagnostico'),
            version=data.get('version')
        )
        diagnostico.save()
        return redirect('diagnosticos_list')
    

@require_http_methods(["PUT"])
def intento_diagnostico(request, diagnostico_id):
    if request.method == "PUT":
        diagnostico = get_object_or_404(Diagnostico, id=diagnostico_id)
        data = json.loads(request.body)
        intento = IntentoDiagnostico(
            diagnostico=diagnostico,
            fecha_intento=data.get('fecha_intento'),
            cambio=data.get('cambio')
        )
        intento.save()
        return redirect('diagnosticos_list')
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@require_http_methods(["GET"])
def intentos_diagnosticos_list(request):
    intentos = IntentoDiagnostico.objects.all()
    data = [{
        "id": str(i.id),
        "diagnostico": str(i.diagnostico.id),
        "fecha_intento": i.fecha_intento.isoformat(),
        "cambio": i.cambio
    } for i in intentos]
    return JsonResponse(data, safe=False)