from ..models import Transaccion


def reconstruccionBaseDeDatos(nueva_vivienda):
   
    return vivienda

def guardarTransaccion(transaccion_guardar):
    transaccion = Transaccion(
        sentenciaTransaccion = transaccion_guardar["sentenciaTransaccion"],
        dateTime = transaccion_guardar["dateTime"],
    )
    transaccion.save()
    return transaccion

def obtenerTransacciones():
    transacciones = []
    transacciones = list(Transaccion.objects.all())
    for transaccion in transacciones:
        sentenciaTransaccion = transaccion["sentenciaTransaccion"]
    return transacciones
