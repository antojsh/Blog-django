from django.shortcuts import render_to_response,redirect
from django.http import HttpResponse
from prueba.models import articulos,usuarios
from django.contrib import admin
from django.template import RequestContext
from prueba.forms import crearArticulo
from django.utils import timezone
# Create your views here. Prueba de Vistas

def index(req):
	Articulos = articulos.objects.all()
	return render_to_response('index.html',{'articulos':Articulos})

def creararticulo(req):
	if req.method == 'POST':
		form = crearArticulo(req.POST)
		if form.is_valid():
			form.save()
			return redirect('/',{'guardado':'Usuario guardado'})
	else:
		form = crearArticulo()
	return render_to_response('creararticulo.html',{'form':form},
		context_instance=RequestContext(req))
