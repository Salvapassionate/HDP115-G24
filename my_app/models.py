# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Misiones(models.Model):
    nombre_mision = models.CharField(max_length=150)
    tipo_mision = models.CharField(max_length=150)
    empresa = models.CharField(max_length=150)
    fecha = models.DateField()
    

    def __str__(self):
        return self.nombre_mision
    class Meta:
        db_table = 'my_app_misiones'
    

