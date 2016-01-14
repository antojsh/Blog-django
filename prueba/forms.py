from django import forms
from prueba.models import usuarios,articulos

class crearArticulo(forms.ModelForm):
	class Meta:
		model = articulos
		fields = '__all__' 