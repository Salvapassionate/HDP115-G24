# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Estadisticas,Ubicacion,Empresa
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, Administrador, Usuario

def mostrar_estadisticas(request):
    estadisticas = Estadisticas.objects.all()
    return render(request, 'index.html', {'estadisticas': estadisticas})

def mostrar_ubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'index.html', {'ubicaciones': ubicaciones})

def mostrar_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'index.html', {'empresas': empresas})
def sistema(request):
    return render(request, 'sistema.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def prueba(request):
    return render(request, 'prueba.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_admin:
                return redirect('index')
            else:
                return redirect('index')
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            error_message = 'Passwords do not match.'
            return render(request, 'register.html', {'error_message': error_message})
        if CustomUser.objects.filter(username=username).exists():
            error_message = 'Username is already taken.'
            return render(request, 'register.html', {'error_message': error_message})
        user = CustomUser.objects.create_user(username=username, password=password)
        return redirect('index')
    else:
        return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')


def home(request):
    estadisticasListadas = Estadisticas.objects.all()
    return render(request, "index.html", {"estadisticas": estadisticasListadas})

def registrar_estadistica(request):
    id = request.POST['txtID']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    edad = request.POST['txtEdad']
    genero = request.POST['txtGenero']
    tipodiscapacidad = request.POST['txtTipoDiscapacidad']
    sector = request.POST['txtSector']
    actividadeconomica = request.POST['txtActividadEconomica']
    categoriaocupacion = request.POST['txtCategoriaOcupacion']

    estadistica = Estadisticas.objects.create(id=id, nombre=nombre, apellido=apellido, edad=edad, genero=genero, tipodiscapacidad=tipodiscapacidad, sector=sector, actividadeconomica=actividadeconomica, categoriaocupacion=categoriaocupacion)
    return redirect('index')

def edicion_estadistica(request, id):
    estadistica = Estadisticas.objects.get(id=id)
    return render(request, 'edicionEstadistica.html', {"estadistica": estadistica})


def editar_estadistica(request):
    id = request.POST['txtID']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    edad = request.POST['txtEdad']
    genero = request.POST['txtGenero']
    tipodiscapacidad = request.POST['txtTipoDiscapacidad']
    sector = request.POST['txtSector']
    actividadeconomica = request.POST['txtActividadEconomica']
    categoriaocupacion = request.POST['txtCategoriaOcupacion']

    estadistica = Estadisticas.objects.get(id=id)
    estadistica.nombre = nombre
    estadistica.apellido = apellido
    estadistica.edad = edad
    estadistica.genero = genero
    estadistica.tipodiscapacidad = tipodiscapacidad
    estadistica.sector = sector
    estadistica.actividadeconomica = actividadeconomica
    estadistica.categoriaocupacion = categoriaocupacion
    estadistica.save()

    return redirect('index')

def eliminar_estadistica(request, id):
    estadistica = Estadisticas.objects.get(id=id)
    estadistica.delete()
    return redirect('index')

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

