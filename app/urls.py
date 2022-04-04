from unicodedata import name
from django.urls import path
from .views import home, login, articulos, contacto, nosotros

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('articulo/', articulos, name="articulos"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros")
]