from distutils.command.upload import upload
import email
from django.db import models


# Create your models here.

opciones_autor = [
    [0, "Admin"],
    [1, "Staff"],
]

opciones_categoria = [
    [0, "Alimentacion"],
    [1, "Medicamentos"],
    [2, "Agenda Medica"],
    [3, "Fonoaudiologia"],
]

class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    categoria = models.IntegerField(choices=opciones_categoria)
    autor = models.IntegerField(choices=opciones_autor)
    texto = models.TextField()
    imagen = models.ImageField(upload_to="publicacion", null=True)

    def __int__(self) :
        return self.id_publicacion


class Paciente(models.Model):
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telfono = models.CharField(max_length=50)
    idTelegram = models.CharField(max_length=50)

    def __str__(self) :
        return self.nombre