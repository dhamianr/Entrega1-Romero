from django.urls import path
from unicodedata import name
from django import urls
from bibliogestion.views import *

urlpatterns = [
    path('',inicio, name="Inicio"),
    path('cliente/',cliente, name="Clientes"),
    path('vendedores/',vendedor, name="Vendedores"),
    path('libros/',cantidad_libros, name="Clibros"),
    path('cargarlibro/',cargar_libro, name="CargarL"),
    path('nuevovendedor/', cargar_vendedor, name="CargarV"),
    path('nuevocliente/',cargar_cliente, name="CargarC"),
    path('busqueda/',busqueda_libro, name="BusquedaL"),
    path('buscar/',buscarL)
    
]
