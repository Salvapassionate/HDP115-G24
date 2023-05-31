# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Misiones
from django.contrib import messages
# Create your views here.

def mostrar_misiones(request):
    misiones = Misiones.objects.all()
    return render(request, 'index.html', {'misiones': misiones})

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    cursosListados = Misiones.objects.all()
    return render(request, "index.html", {"misiones": cursosListados})


def registrarCurso(request):
    id = request.POST['txtId']
    nombre_mision = request.POST['txtMision']
    tipo_mision = request.POST['txtTipo']
    empresa = request.POST['txtEmpresa']
    fecha = request.POST['txtFecha']

    curso = Misiones.objects.create(id=id, nombre_mision=nombre_mision, tipo_mision=tipo_mision, empresa=empresa, fecha=fecha)
    return redirect('/')


def edicionCurso(request, id):
    curso = Misiones.objects.get(id=id)
    return render(request, "edicionCurso.html", {"curso": curso})  # Cambio aquí


def editarCurso(request):
    id = request.POST['txtId']
    nombre_mision = request.POST['txtMision']
    tipo_mision = request.POST['txtTipo']
    empresa = request.POST['txtEmpresa']
    fecha = request.POST['txtFecha']

    curso = Misiones.objects.get(id=id)
    curso.nombre_mision = nombre_mision
    curso.tipo_mision = tipo_mision
    curso.empresa = empresa
    curso.fecha = fecha
    curso.save()

    return redirect('/')


def eliminarCurso(request, id):
    curso = Misiones.objects.get(id=id)
    curso.delete()
    return redirect('/')

