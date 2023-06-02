
from django.db.models.signals import post_migrate 
from django.dispatch import receiver
from .models import Estadisticas
from django.contríb.auth.hashers import make_password

@receiver(post_migrate)
def crear_instancias_estadisticas(sender, **kwargs):
    if sender.name == 'my_app':
        if not Estadisticas.objects.exists():
            instancias = [
            {'nombre':'Jose','apelllido': 'Barrera', 'edad': '45' , 'genero': 'Masculino', 'tipodiscapacidad':'Auditiva' , 'sector': 'comercio', 'actividadeconomica':'Actividades inmobiliarias', 'categoriaocupacion':'Ocupaciones elemntales' },
            {'nombre': 'Juan', 'apellido': 'Pérez', 'edad': '35', 'genero': 'Masculino', 'tipodiscapacidad': 'Motriz', 'sector': 'Servicios', 'actividadeconomica': 'Consultoría', 'categoriaocupacion': 'Profesionales'}

           
            ]
        for instancia in instancias:
            instancia['contrasenia'] = make_password(instancia['contrasenia'])
            Estadisticas.objects.create(nombre=instancia[ 'nombre' ], apellido=instancia[ 'apellido' ],edad=instancia[ 'edad' ], genero=instancia[ 'genero' ],tipodiscapacidad=instancia[ 'tipodiscapacidad' ], sector=instancia[ 'sector' ], comercio=instancia[ 'comercio' ],actividadeconomica=instancia[ 'actividadeconomica'],categoriaocupacion=instancia[ 'categoriaocupacion' ])

