
from ..models import Psicologo, Calificacion

def get_psicologo(id):
    psicologo = Psicologo.objects.get(pk=id)
    return psicologo

def create_psicologo(nuevo_psicologo):
    psicologo = Psicologo(nombre=nuevo_psicologo["nombre"])
    psicologo.save()
    return psicologo  

def add_calificacionpsicologo(id, puntuacion):
    psicologo = Psicologo.objects.get(pk=id)
    psicologo.suma_calificaciones += puntuacion
    psicologo.cantidad_calificaciones += 1 
    psicologo.promedio_calificaciones =  psicologo.suma_calificaciones / psicologo.cantidad_calificaciones
    psicologo.save() 
    return psicologo


def get_calificaciones():
    calificaciones = Calificacion.objects.all()
    return calificaciones

def get_calificacion(id):
    calificaciones = Calificacion.objects.get(id)
    return calificaciones    

def create_calificacion(nueva_calificacion, id_psicologo):
    calificacion = Calificacion(psicologo=get_psicologo(id_psicologo), mensaje=nueva_calificacion["mensaje"], puntuacion = nueva_calificacion["puntuacion"])
    calificacion.save()
    add_calificacionpsicologo(id_psicologo,nueva_calificacion["puntuacion"])
    return calificacion