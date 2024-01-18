from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hola, Mundo")
                        #"Hola, Mundo" es lo que imprime al ponerle /Practica despues del URL
def brian(request):
    return HttpResponse("Hola, Brian")

def david(request):
    return HttpResponse("Hola, David")