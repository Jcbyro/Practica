import datetime
from django.shortcuts import render

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, 'Newyear/index.html', {
        'Newyear': now.month == 1 and now.day == 1
    })
        # Puedo remplazar 'Newyear": ... por 'Newyear': True
                                            # Esta nueva funcion hace que al salir un resultado me de lo opuesto, es decir si es Newyear entonces dice NO