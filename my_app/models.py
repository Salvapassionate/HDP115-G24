# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Creado el models login

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='customuser_set')


class Administrador(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Usuario(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

# Create your models here.
class Estadisticas(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.CharField(max_length=50)
    tipodiscapacidad = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    actividadeconomica = models.CharField(max_length=100)
    categoriaocupacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table ='my_app_estadisticas'

class Ubicacion(models.Model):
    nombreUb = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    coordenadaX = models.DecimalField(max_digits=9, decimal_places=6)
    coordenadaY = models.DecimalField(max_digits=9, decimal_places=6)
    
    def __str__(self):
        return self.nombreUb
    
    class Meta:
        db_table = 'my_app_ubicaciones'

class Empresa(models.Model):
    nombreE = models.CharField(max_length=100)
    direccionE = models.CharField(max_length=200)
    correoE = models.EmailField()
    telefonoE = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreE
    
    class Meta:
        db_table = 'empresas'
