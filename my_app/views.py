# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Misiones

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

