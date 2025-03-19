from django.shortcuts import render
from .models import Proyecto, Contacto
from django.http import HttpResponseRedirect
from django.urls import reverse

# Vista de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista de proyectos
def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})

# Vista de acerca de nosotros
def acerca_de_nosotros(request):
    return render(request, 'about.html')

# Vista de contacto
def contacto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        mensaje = request.POST['mensaje']
        Contacto.objects.create(nombre=nombre, correo=correo, mensaje=mensaje)
        return HttpResponseRedirect(reverse('contacto'))  # Redirige después de guardar

    return render(request, 'contacto.html')