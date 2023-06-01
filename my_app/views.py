# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Estadisticas
from django.contrib import messages

def mostrar_estadisticas(request):
    estadisticas = Estadisticas.objects.all()
    return render(request, 'index.html', {'estadisticas': estadisticas})

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    estadisticasListadas = Estadisticas.objects.all()
    return render(request, "index.html", {"estadisticas": estadisticasListadas})

def registrar_estadistica(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    edad = request.POST['txtEdad']
    genero = request.POST['txtGenero']
    tipodiscapacidad = request.POST['txtTipoDiscapacidad']
    sector = request.POST['txtSector']
    actividadeconomica = request.POST['txtActividadEconomica']
    categoriaocupacion = request.POST['txtCategoriaOcupacion']

    estadistica = Estadisticas.objects.create(nombre=nombre, apellido=apellido, edad=edad, genero=genero, tipodiscapacidad=tipodiscapacidad, sector=sector, actividadeconomica=actividadeconomica, categoriaocupacion=categoriaocupacion)
    return redirect('/')

def edicion_estadistica(request, nombre):
    estadistica = Estadisticas.objects.get(nombre=nombre)
    return render(request, "edicionEstadistica.html", {"estadistica": estadistica})

def editar_estadistica(request):
    """id = request.POST['txtId']"""
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    edad = request.POST['txtEdad']
    genero = request.POST['txtGenero']
    tipodiscapacidad = request.POST['txtTipoDiscapacidad']
    sector = request.POST['txtSector']
    actividadeconomica = request.POST['txtActividadEconomica']
    categoriaocupacion = request.POST['txtCategoriaOcupacion']

    estadistica = Estadisticas.objects.get(nombre=nombre)
    estadistica.apellido = apellido
    estadistica.edad = edad
    estadistica.genero = genero
    estadistica.tipodiscapacidad = tipodiscapacidad
    estadistica.sector = sector
    estadistica.actividadeconomica = actividadeconomica
    estadistica.categoriaocupacion = categoriaocupacion
    estadistica.save()

    return redirect('/')

def eliminar_estadistica(request, nombre):
    estadistica = Estadisticas.objects.get(nombre=nombre)
    estadistica.delete()
    return redirect('/')
