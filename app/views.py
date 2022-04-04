from django.shortcuts import render
from .models import Publicacion

# Create your views here.

def home(request):
    publicacion = Publicacion.objects.all()
    data = {
            'publicacion' : publicacion
    }
        
    
    return render(request, 'app/home.html', data)
    

def login(request):
    return render(request, 'app/login.html')


def articulos(request):
    return render(request, 'app/articulos.html')


def contacto(request):
    return render(request, 'app/contacto.html')


def nosotros(request):
    return render(request, 'app/nosotros.html')