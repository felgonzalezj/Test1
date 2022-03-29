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