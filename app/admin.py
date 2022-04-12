from django.contrib import admin
from .models import Publicacion , Paciente, Paciente_Fonoaudiologia

# Register your models here.

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ["id_publicacion", "titulo", "fecha_publicacion", "categoria", "autor", "texto", "imagen"]

class PacienteAdmin(admin.ModelAdmin):
    list_display = ["rut", "nombre", "apellidos", "email", "telfono", "idTelegram"]

class Paciente_Fono_Admin(admin.ModelAdmin):
    list_display = ["rut", "fecha", "audio_wav", "video", "feedback"]



admin.site.register(Publicacion , PublicacionAdmin)
admin.site.register(Paciente , PacienteAdmin)
admin.site.register(Paciente_Fonoaudiologia, Paciente_Fono_Admin)