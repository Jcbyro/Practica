from django.urls import path
from . import views

urlpatterns = {
    path("", views.index, name="index")
    # ("") un string que representa el URL
    # (views.index) Una funcion de views.py que se quiere llamar al visitar el URL
    # (name="index") Un nombre para el URL
}