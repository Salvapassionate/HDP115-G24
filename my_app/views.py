# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Misiones

# Create your views here.

def mostrar_misiones(request):
    if request.method == 'POST':
        if 'editar_mision' in request.POST:
            mision_id = request.POST['editar_mision']
            return redirect('editar_mision', mision_id=mision_id)
        elif 'eliminar_mision' in request.POST:
            mision_id = request.POST['eliminar_mision']
            return redirect('eliminar_mision', mision_id=mision_id)
    misiones = Misiones.objects.all()
    return render(request, 'index.html', {'misiones': misiones})

def editar_mision(request, mision_id):
    mision = Misiones.objects.get(id=mision_id)

    if request.method == 'POST':
        # Obtener los datos actualizados del formulario
        nombre_mision = request.POST['nombre_mision']
        tipo_mision = request.POST['tipo_mision']
        empresa = request.POST['empresa']
        fecha = request.POST['fecha']

        # Actualizar los campos de la misión
        mision.nombre_mision = nombre_mision
        mision.tipo_mision = tipo_mision
        mision.empresa = empresa
        mision.fecha = fecha
        mision.save()

        return redirect('misiones') # Redirigir a la página de misiones

    return render(request, 'index.html', {'mision': mision})


def eliminar_mision(request, mision_id):
    mision = Misiones.objects.get(id=mision_id)

    if request.method == 'POST':
        mision.delete()
        return redirect('misiones')  # Redirigir a la página de misiones

    return render(request, 'index.html', {'mision': mision})

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

