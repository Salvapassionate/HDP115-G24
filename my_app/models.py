# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
        db_table = 'my_app_estadisticas'
