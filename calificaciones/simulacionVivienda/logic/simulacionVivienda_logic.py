from ..models import Vivienda, Transporte, Consulta


def get_vivienda(id):
    vivienda = Vivienda.objects.get(pk=id)
    return vivienda

def create_vivienda(nueva_vivienda):
    vivienda = Vivienda(nombre = nueva_vivienda["nombre"],
    precio = nueva_vivienda["precio"],
    parqueadero = nueva_vivienda["parqueadero"],
    pagoPorSemestre = nueva_vivienda["pagoPorSemestre"],
    distanciaAlaUniversidad = nueva_vivienda["distanciaAlaUniversidad"])
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


def get_consulta(nueva_consulta):
    consulta = Consulta(
        precioMaximo = nueva_consulta["precioMaximo"],
        distanciaAlaUniversidad = nueva_consulta["distanciaAlaUniversidad"],
        parqueadero = nueva_consulta["parqueadero"]
    )
     
    viviendasValidas = Vivienda.objects.all().filter(precio = consulta.precioMaximo, distanciaAlaUniversidad = consulta.distanciaAlaUniversidad, parqueadero = consulta.parqueadero)
    return viviendasValidas


