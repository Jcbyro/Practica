from django.urls import path
from . import views

app_name = "Newyear"
urlpatterns = [
    path('', views.index, name='index'),
]