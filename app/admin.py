from django.contrib import admin
from .models import Publicacion , Paciente

# Register your models here.

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ["id_publicacion", "titulo", "fecha_publicacion", "categoria", "autor", "texto", "imagen"]

class PacienteAdmin(admin.ModelAdmin):
    list_display = ["rut", "nombre", "apellidos", "email", "telfono", "idTelegram"]



admin.site.register(Publicacion , PublicacionAdmin)
admin.site.register(Paciente , PacienteAdmin)