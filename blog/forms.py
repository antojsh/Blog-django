from django import forms

class Login(forms.Form):
	usuario =forms.CharField()
	password= forms.CharField(widget=form.PasswordInput())