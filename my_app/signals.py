"""
from django.db.models.signals import post_migrate 
from django.dispatch import receiver
from .models import Administrador
from django.contríb.auth.hashers import make_password

©receiver(post_migrate)
def crear_instancias_administrador(sender, **kwargs):
if sender.name == 'my_app':
if not Administrador.objects.exists():
instancias = [
{'email':'correo1', 'contrasenía': 'contra1' },
{'email':'correo2', 'contrasenía': 'contra2' },
{'email':'correo3', 'contrasenía': 'contra3' },
for instancia in instancias:
instancia['contrasenia'] = make_password(instancia['contrasenia'])
Adminístrador.objects.create(email=instancia[ 'email' ], contrasenia=instancia[ 'contrasenia' ])
]
"""