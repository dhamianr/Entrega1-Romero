from pyexpat import model
from django.db import models

# Create your models here.
class Vendedor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    num_dni = models.IntegerField(primary_key=True)

class Cliente(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    num_dni = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=20)

class Libro(models.Model):

    nombre = models.CharField(max_length=15)
    autor = models.CharField(max_length=10)
    genero = models.CharField(max_length=10)
    isbn = models.IntegerField(primary_key=True)
    cantidad = models.IntegerField(default=0)

