from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from bibliogestion.forms import CargarLibro, CargarCliente, CargarVendedor
from bibliogestion.models import Libro, Cliente, Vendedor

# Create your views here.

def inicio(request):
    return render(request,"bibliogestion/index.html")

def cliente(request):
    return render(request,"bibliogestion/cliente.html")

def vendedor(request):
    return render(request,"bibliogestion/vendedor.html")

def cantidad_libros(request):
    return render(request,"bibliogestion/cant_libro.html")

def cargar_libro(request):

    if request.method == "POST":
        cantidad = CargarLibro(request.POST)

        if cantidad.is_valid():
            data = cantidad.cleaned_data

            cantidad_nueva = Libro(request.POST['nombre'],request.POST['autor'],request.POST['genero'],request.POST['isbn'],request.POST['cantidad'])
            cantidad_nueva.save()

        return render(request, "bibliogestion/index.html")
    else:
        cantidad_form = CargarLibro()

    return render(request, "bibliogestion/cargar_libro.html", {"formulario": cantidad_form})

def cargar_vendedor(request):
    if request.method == "POST":
        vendedor = CargarVendedor(request.POST)

        if vendedor.is_valid():
            data = vendedor.cleaned_data

            nuevo_vendedor = Libro(data['nombre'],data['apellido'],data['num_dni'])
            nuevo_vendedor.save()

            vendedor = CargarVendedor()
            return render(request, "bibliogestion/index.html")
    else:
        vendedor_form = CargarVendedor()
        return render(request, "bibliogestion/nuevo_vendedor.html", {"formulario": vendedor_form})

def cargar_cliente(request):

    if request.method == "POST":
        cliente = CargarCliente(request.POST)

        if cliente.is_valid:
            data = cliente.cleaned_data

            nuevo_cliente = Libro(nombre = data['nombre'],apellido = data['apellido'],num_dni = data['num_dni'],email = data['email'])
            nuevo_cliente.save()

        return render(request, "bibliogestion/index.html")
    else:
        cliente_form = CargarVendedor()

    return render(request, "bibliogestion/nuevo_cliente.html", {"formulario": cliente_form})

def busqueda_libro(request):
    return render(request,"bibliogestion/busquedalibro.html")

def buscarL(request):
    
    data = request.GET.get('isbn', "")
    error = ""

    if data:
        try:
            libro = Libro.objects.get(isbn__icontains=data) #probe con un objects.filter como en las diapo, pero tampoco busca
            return render(request, 'bibliogestion/busquedalibro.html', {"libro": libro, "data": data})

        except Exception as exc:
            print(exc)
            error = "No existe ese libro"
    return render(request, 'bibliogestion/busquedalibro.html', {"error": error})
