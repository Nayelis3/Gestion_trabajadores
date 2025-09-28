from django.contrib import admin
from .models import Trabajador, Documento

# Register your models here.
@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "puesto")

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("id", "trabajador", "archivo")