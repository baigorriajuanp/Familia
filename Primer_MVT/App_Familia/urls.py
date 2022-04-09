from django import views
from django.urls import path
from .views import inicio, carga_familiar, mostrar_familia

urlpatterns = [
    path('',inicio, name="Inicio"),
    path('carga_familiares/',carga_familiar, name="Cargar_Familiar"),
    path('ver_familiares/',mostrar_familia, name="Ver_Familiares"),
]