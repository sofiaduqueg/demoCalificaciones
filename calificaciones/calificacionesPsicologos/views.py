from .logic import calificacionespsicologos_logic as cl
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def psicologo_view(request,id):
    if request.method == 'GET':
        psicologo_dto = cl.get_psicologo(id)
        psicologo = serializers.serialize('json',[psicologo_dto,])
        return HttpResponse(psicologo, 'application/json')

    
@csrf_exempt
def psicologo_view_noid(request):
    if request.method == 'POST':
        psicologo_dto = cl.create_psicologo(json.loads(request.body))
        psicologo = serializers.serialize('json', [psicologo_dto,])
        return HttpResponse(psicologo, 'application/json')

@csrf_exempt
def calificacion_view(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')
