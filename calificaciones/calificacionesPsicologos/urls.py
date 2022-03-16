from django.urls import path 
from . import views

urlpatterns = [
    path('', views.psicologo_view_noid, name='psicologo_view_noid'),
    path('<int:id>', views.psicologo_view, name='psicologo_view'),
    path("calificacion/<int:id_psicologo>", views.calificacion_view, name='calificacion_view')

]

