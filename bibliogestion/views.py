from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from bibliogestion.forms import CargarLibro, CargarCliente, CargarVendedor
from bibliogestion.models import Libro, Cliente, Vendedor

# Create your views here.

def inicio(request):
    return render(request,"bibliogestion/index.html")

# def cliente(request):
#     return render(request,"bibliogestion/cliente.html")

# def vendedor(request):
#     return render(request,"bibliogestion/vendedor.html")

# def cantidad_libros(request):
#     return render(request,"bibliogestion/cant_libro.html")

def cargar_libro(request):

    if request.method == "POST":
        cantidad = CargarLibro(request.POST)

        if cantidad.is_valid():
            data = cantidad.cleaned_data

            cantidad_nueva = Libro(data['nombre'],data['autor'],data['genero'],data['isbn'],data['cantidad'])
            cantidad_nueva.save()
            cantidad = CargarLibro()
            return render(request, "bibliogestion/cant_libro.html",{"formulario": cantidad})
    else:
        cantidad_form = CargarLibro()
        return render(request, "bibliogestion/cant_libro.html", {"formulario": cantidad_form})

def cargar_vendedor(request):

    vendedor = Vendedor.objects.all()

    if request.method == "POST":
        vendedores = CargarVendedor(request.POST)

        if vendedores.is_valid():
            data = vendedores.cleaned_data

            nuevo_vendedores = Vendedor(data['nombre'],data['apellido'],data['num_dni'])
            nuevo_vendedores.save()

            vendedores = CargarVendedor()
            return render(request, "bibliogestion/vendedor.html", {"vendedor": vendedor, "formulario": vendedores})
    else:
        vendedores = CargarVendedor()
        return render(request, "bibliogestion/vendedor.html", {"vendedor": vendedor,"formulario": vendedores})

def cargar_cliente(request):

    if request.method == "POST":
        cliente = CargarCliente(request.POST)

        if cliente.is_valid():
            data = cliente.cleaned_data

            cliente = CargarCliente(data['nombre'],data['apellido'],data['num_dni'],data['email'])
            cliente.save()

            cliente = CargarCliente()
            return render(request, "bibliogestion/index.html")
    else:
        cliente_form = CargarCliente()
        return render(request, "bibliogestion/nuevo_cliente.html", {"formulario": cliente_form})

def buscarL(request):
    
    data = request.GET.get('isbn', "")
    error = ""

    if data:
        try:
            libro = Libro.objects.get(isbn__icontains=data) 
            return render(request, 'bibliogestion/busquedalibro.html', {"nombre": libro, "data": data})
        except Exception as exc:
            print(exc)
            error = "No existe ese libro"
    return render(request, 'bibliogestion/busquedalibro.html', {"error": error})
