import django
django.setup()
import os

from aplicacion.models import Usuario, Fichero, Acceso
from django.test import SimpleTestCase
from django.utils import timezone
from datetime import timedelta
from proyecto.settings import BASE_DIR
pathToProject = BASE_DIR
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'proyecto.settings')


class QueryTestUsers(SimpleTestCase):
    allow_database_queries = True

    def erase_all(self):
        Usuario.objects.all().delete()
        Fichero.objects.all().delete()
        Acceso.objects.all().delete()

    def test_create_user1001(self):
        try:
            Usuario.objects.get(id=1001)
        except:
            user_1001 = Usuario.objects.create(id=1001, nombreU="usuario1")
            user_1001.save()
            self.assertEqual(user_1001, Usuario.objects.get(id=1001))

    def test_create_user1002(self):
        try:
            Usuario.objects.get(id=1002)
        except:
            user_1002 = Usuario.objects.create(id=1002, nombreU="usuario2")
            user_1002.save()
            self.assertEqual(user_1002, Usuario.objects.get(id=1002))

    def test_create_fichero1001(self):
        try:
            Fichero.objects.get(id=1001)
        except:
            user_1001 = Usuario.objects.create(id=1001, nombreU="usuario1")
            user_1001.save()
            self.assertEqual(user_1001, Usuario.objects.get(id=1001))
            fichero_1001 = Fichero.objects.create(id=1001, nombreF="eee.txt", usuario=Usuario.objects.get(id=1001))
            fichero_1001.save()
            self.assertEqual(fichero_1001, Fichero.objects.get(id=1001))

    def test_create_acceso1001(self):
        try:
            Acceso.objects.get(id=1001)
        except:
            user_1002 = Usuario.objects.create(id=1002, nombreU="usuario2")
            user_1002.save()
            self.assertEqual(user_1002, Usuario.objects.get(id=1002))
            fichero_1001 = Fichero.objects.create(id=1001, nombreF="eee.txt", usuario=Usuario.objects.get(id=1002))
            fichero_1001.save()
            self.assertEqual(fichero_1001, Fichero.objects.get(id=1001))
            acceso_1001 = Acceso.objects.create(id=1001, usuario=Usuario.objects.get(id=1002), fichero=Fichero.objects.get(id=1001), fecha='2021-01-25', modo="read")
            acceso_1001.save()
            self.assertEqual(acceso_1001, Acceso.objects.get(id=1001))


