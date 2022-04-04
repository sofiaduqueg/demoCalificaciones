from django.urls import path 
from . import views

urlpatterns = [
    path('crearVivienda/',views.vivienda_view_create,name="vivienda_view_create"),
    path('consultarVivienda/<int:id>',views.vivienda_view, name="vivienda_view"),
    path('crearTransporte/<int:id_vivienda>', views.transporte_view, name="transporte_view" ),
    path('consultarTransportes/<int:id_vivienda>', views.transportes_vivienda_view, name="transportes_vivienda_view")
]