from .logic import logDeTransacciones_logic as vl
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def transaccion_view(request):
    if request.method == 'POST':
        transaccion_dto = vl.reconstruccionBaseDeDatos(json.loads(request.body))   
        transaccion = serializers.serialize('json', [transaccion_dto,])
        return HttpResponse(transaccion,'application/json')

@csrf_exempt
def transaccion_view_guardar(request):
    if request.method == 'POST':
        transaccion_dto = vl.guardarTransaccion(json.loads(request.body))   
        transaccion = serializers.serialize('json', [transaccion_dto,])
        return HttpResponse(transaccion,'application/json')
