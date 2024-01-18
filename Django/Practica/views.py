from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def index(request):
    #return HttpResponse("<h1 style=\"color:red\">Hola, Mundo</h1>")
                        #"Hola, Mundo" es lo que imprime al ponerle /Practica despues del URL

def index(request):
    return render(request, "Practica/index.html")

#def brian(request):
    return HttpResponse("Hola, Brian")
    #Es mas oscuro por que representa que ya no sirve
#def david(request):
    return HttpResponse("Hola, David")

#def greet(request, name):
    return HttpResponse(f"Hola, {name.capitalize()}")
                                #.capitalize() hace que la primera palabra ahora este en mayuscula

def greet(request, name):
    return render(request, "Practica/greet.html", {
        "name": name.capitalize()
    })