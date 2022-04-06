from django.contrib import admin
from bibliogestion.models import Libro,Vendedor,Cliente

# Register your models here.

admin.site.register(Vendedor)
admin.site.register(Cliente)
admin.site.register(Libro)