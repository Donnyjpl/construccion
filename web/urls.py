from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('acerca-de-nosotros/', views.acerca_de_nosotros, name='acerca_de_nosotros'),
    path('contacto/', views.contacto, name='contacto'),
]