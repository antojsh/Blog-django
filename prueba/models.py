from __future__ import unicode_literals

from django.db import models

# Create your models here.


class usuarios(models.Model):
	usuario  	= models.TextField(default='')
	nombre 		= models.CharField(max_length=300)
	sexo 		= models.CharField(max_length=1)
	

class articulos(models.Model):
	nombre 		= models.CharField(max_length=300)
	descripcion = models.TextField()
	fecha 		= models.DateTimeField(auto_now_add=True)
	usuario 	= models.ForeignKey(usuarios,null=True)
	def __str__(self):
		return self.nombre









	