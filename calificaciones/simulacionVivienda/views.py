from .logic import simulacionVivienda_logic as vl
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def vivienda_view(request, id):
    if request.method == 'GET':
        vivienda_dto = vl.get_vivienda(id)
        vivienda = serializers.serialize('json', [vivienda_dto,])
        return HttpResponse(vivienda,'application/json')

@csrf_exempt
def vivienda_view_create(request):
    if request.method == 'POST':
        vivienda_dto = vl.create_vivienda(json.loads(request.body))   
        vivienda = serializers.serialize('json', [vivienda_dto,])
        return HttpResponse(vivienda,'application/json')


@csrf_exempt
def transporte_view(request, id_vivienda):
    if request.method == 'POST':
        transporte_dto = vl.create_transporte(json.loads(request.body),id_vivienda)
        transporte = serializers.serialize('json', [transporte_dto,])
        return HttpResponse(transporte, 'application/json')

@csrf_exempt
def transportes_vivienda_view(request, id_vivienda):
    if request.method == 'GET':
        transportes= vl.get_transportesVivienda(id_vivienda)
        return HttpResponse(transportes, 'application/json')        


