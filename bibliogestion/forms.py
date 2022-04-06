from django import forms

class CargarLibro(forms.Form):
    # Campos de datos

    nombre = forms.CharField(max_length=15)
    autor = forms.CharField(max_length=10)
    genero = forms.CharField(max_length=10)
    isbn = forms.IntegerField()
    cantidad = forms.IntegerField()

class CargarCliente(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=20)
    num_dni = forms.IntegerField()
    email = forms.EmailField()

class CargarVendedor(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=20)
    num_dni = forms.IntegerField()


