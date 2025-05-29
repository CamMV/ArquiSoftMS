import json
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Diagnostico, IntentoDiagnostico
from datetime import datetime
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
        resultado = request.POST.get('resultado')
        diagnostico = request.POST.get('diagnostico')

        diagnostico = Diagnostico(resultado=resultado, diagnostico=diagnostico, fecha_diagnostico=datetime.now(), version="1.0")
        diagnostico.save()
        return redirect('diagnosticos_list')
    else:
        return render(request, 'Diagnostico/diagnosticoCreate.html')

@require_http_methods(["POST"])
def intento_diagnostico(request, diagnostico_id):
    if request.method == "POST":
        try:
            diagnostico = Diagnostico.objects.get(id=diagnostico_id)
        except DoesNotExist:
            return JsonResponse({"error": "Diagnostico not found"}, status=404)
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
    return JsonResponse(
        {"intentos": [intento.to_json() for intento in intentos]},
        safe=False
    )