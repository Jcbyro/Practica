#Este se crea cada vez que queres una aplicacion individual

from django.urls import path
# Nos da la abilidad de desviar el URL
from . import views
# Importa cualquier funcion que se creo en views.py

urlpatterns = [
    path('', views.index, name='index'),
    # ("") un string que representa el URL
    # (views.index) Una funcion de views.py que se quiere llamar al visitar el URL
    # (name='index') Un nombre para el URL
    
    #path('brian', views.brian, name='brian'),
    #path('david', views.david, name='david'),
    #Otra forma de poner estos 2 paths es con lo siguente
    path('<str:name>', views.greet, name='greet'),
    #Este nuevo path agarra cualquier nombre y te lo imprime como "Hola, nuevo_nombre"
]