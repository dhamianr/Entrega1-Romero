from django.urls import path
from unicodedata import name
from django import urls
from bibliogestion.views import *

urlpatterns = [
    path('',inicio, name="Inicio"),
    path('libros/',cargar_libro, name="CargarL"),
    path('vendedor/', cargar_vendedor, name="CargarV"),
    path('cliente/',cargar_cliente, name="CargarC"),
    path('buscar/',buscarL, name= "BuscarL")
    
]
