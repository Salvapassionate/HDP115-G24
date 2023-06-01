# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Estadisticas,Ubicacion,Empresa
from django.contrib import messages

def mostrar_estadisticas(request):
    estadisticas = Estadisticas.objects.all()
    return render(request, 'index.html', {'estadisticas': estadisticas})

def mostrar_ubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'index.html', {'ubicaciones': ubicaciones})

def mostrar_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'index.html', {'empresas': empresas})

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

def home_ubicacion(request):
    ubicacionesListadas = Ubicacion.objects.all()
    return render(request, "index.html", {"ubicaciones": ubicacionesListadas})

def registrar_ubicacion(request):
    nombreUB = request.POST['txtnombreUB']
    departamento = request.POST['txtdepartamento']
    municipio = request.POST['txtmunicipio']
    coordenadaX = request.POST['txtcoordenadaX']
    coordenadaY = request.POST['txtcoordenadaY']

    ubicacion = Ubicacion.objects.create(nombreUB=nombreUB, departamento=departamento, municipio=municipio, coordenadaX=coordenadaX, coordenadaY=coordenadaY)
    return redirect('/')

def edicion_ubicacion(request, nombre):
    ubicacion = Ubicacion.objects.get(nombreUB=nombre)
    return render(request, "edicionUbicacion.html", {"ubicacion": ubicacion})

def editar_ubicacion(request):
    nombreUB = request.POST['txtnombreUB']
    departamento = request.POST['txtdepartamento']
    municipio = request.POST['txtmunicipio']
    coordenadaX = request.POST['txtcoordenadaX']
    coordenadaY = request.POST['txtcoordenadaY']

    ubicacion = Ubicacion.objects.get(nombreUB=nombreUB)
    ubicacion.departamento = departamento
    ubicacion.municipio = municipio
    ubicacion.coordenadaX = coordenadaX
    ubicacion.coordenadaY = coordenadaY
    ubicacion.save()

    return redirect('/')

def eliminar_ubicacion(request, nombre):
    ubicacion = Ubicacion.objects.get(nombreUB=nombre)
    ubicacion.delete()
    return redirect('/')

from .models import Empresa

def home_empresa(request):
    empresasListadas = Empresa.objects.all()
    return render(request, "index.html", {"empresas": empresasListadas})

def registrar_empresa(request):
    nombreE = request.POST['txtNombreE']
    direccionE = request.POST['txtDireccionE']
    correoE = request.POST['txtCorreoE']
    telefonoE = request.POST['txtTelefonoE']

    empresa = Empresa.objects.create(nombreE=nombreE, direccionE=direccionE, correoE=correoE, telefonoE=telefonoE)
    return redirect('/')

def edicion_empresa(request, nombre):
    empresa = Empresa.objects.get(nombreE=nombre)
    return render(request, "edicionEmpresa.html", {"empresa": empresa})

def editar_empresa(request):
    nombreE = request.POST['txtNombreE']
    direccionE = request.POST['txtDireccionE']
    correoE = request.POST['txtCorreoE']
    telefonoE = request.POST['txtTelefonoE']

    empresa = Empresa.objects.get(nombreE=nombreE)
    empresa.direccionE =  direccionE
    empresa.correoE = correoE
    empresa.telefonoE = telefonoE 
    empresa.save()

    return redirect('/')

def eliminar_empresa(request, nombreE):
    empresa = Empresa.objects.get(nombreE=nombreE)
    empresa.delete()
    return redirect('/')

