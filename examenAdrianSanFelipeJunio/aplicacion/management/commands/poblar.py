import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')
import django
django.setup()
from aplicacion.models import Usuario, Fichero, Acceso
from django.core.management.base import BaseCommand
import datetime

class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		Usuario.objects.all().delete()
		Fichero.objects.all().delete()
		Acceso.objects.all().delete()

		usuarioD=[
		{'id':'1001', 'nombreU':'usuario_01'},
		{'id':'1002', 'nombreU':'usuario_02'},
		{'id':'1003', 'nombreU':'usuario_03'}
		]

		ficheroD=[
		{'id':'1001', 'nombreF':'aaa.txt', 'usuario':'1002'},
		{'id':'1002', 'nombreF':'bbb.txt', 'usuario':'1001'},
		{'id':'1003', 'nombreF':'ccc.txt', 'usuario':'1003'},
		{'id':'1004', 'nombreF':'ddd.txt', 'usuario':'1002'}
		]

		accesoD=[
		{'id':'1001', 'usuario':'1001', 'fichero':'1003', 'fecha':'2021-01-05', 'modo':'read'},
		{'id':'1002', 'usuario':'1001', 'fichero':'1001', 'fecha':'2021-01-11', 'modo':'update'},
		{'id':'1003', 'usuario':'1002', 'fichero':'1003', 'fecha':'2021-01-12', 'modo':'read'},
		{'id':'1004', 'usuario':'1003', 'fichero':'1002', 'fecha':'2021-01-16', 'modo':'add'}
		]

		for usuariop in usuarioD:
			u=Usuario.objects.get_or_create(id=usuariop['id'], nombreU=usuariop['nombreU'])[0]
			u.save()

		for ficherop in ficheroD:
			f=Fichero.objects.get_or_create(id=ficherop['id'], nombreF=ficherop['nombreF'], usuario=Usuario.objects.get_or_create(id=ficherop['usuario'])[0])[0]
			f.save()

		for accesop in accesoD:
			a=Acceso.objects.get_or_create(id=accesop['id'], usuario=Usuario.objects.get_or_create(id=accesop['usuario'])[0], 
			fichero=Fichero.objects.get_or_create(id=accesop['fichero'])[0], fecha=accesop['fecha'], modo=accesop['modo'])[0]
			a.save()
