from django import forms

class registros(forms.Form):

	nombre=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),required=True)
	clave=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','type':'password'}),required=True)
	telefono=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),required=True,max_length=9,min_length=9)

class logins(forms.Form):
	nombre=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),required=True)
	clave=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','type':'password'}),required=True)