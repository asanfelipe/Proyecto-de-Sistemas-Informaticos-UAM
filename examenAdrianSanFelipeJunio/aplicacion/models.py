from django.db import models

class Usuario(models.Model):
	nombreU=models.CharField(max_length=50)

	def __str__(self):
		return self.id.__str__()+", "+self.nombreU

class Fichero(models.Model):
	nombreF=models.CharField(max_length=50)
	usuario=models.ForeignKey('Usuario', null=True, default="", on_delete=models.CASCADE)

	def __str__(self):
		return self.id.__str__()+", "+self.nombreF+", "+self.usuario.id.__str__()

class Acceso(models.Model):
	usuario=models.ForeignKey('Usuario', null=True, default="", on_delete=models.CASCADE)
	fichero=models.ForeignKey('Fichero', null=True, default="", on_delete=models.CASCADE)
	fecha=models.DateField(auto_now=False, auto_now_add=False)
	modo=models.CharField(max_length=50)

	def __str__(self):
		return self.id.__str__()+", "+self.usuario.id.__str__()+", "+self.fichero.id.__str__()+", "+self.fecha.__str__()+", "+self.modo
