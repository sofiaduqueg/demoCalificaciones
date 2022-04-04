from ..models import Vivienda, Transporte


def get_vivienda(id):
    vivienda = Vivienda.objects.get(pk=id)
    return vivienda

def create_vivienda(nueva_vivienda):
    vivienda = Vivienda(nombre = nueva_vivienda["nombre"],
    precio = nueva_vivienda["precio"],
    parqueadero = nueva_vivienda["parqueadero"],
    pagoPorSemestre = nueva_vivienda["pagoPorSemestre"])
    vivienda.save()
    return vivienda

def create_transporte(nuevo_transporte, id_vivienda):
    transporte = Transporte(
        vivienda = Vivienda.objects.get(pk=id_vivienda),
        nombre = nuevo_transporte["nombre"],
        precio = nuevo_transporte["precio"],
        idDeVivienda = id_vivienda
    )
    transporte.save()
    return transporte

def get_transportesVivienda(id_vivienda):
    transportes = Transporte.objects.all().filter(idDeVivienda = id_vivienda)
    return transportes

    



