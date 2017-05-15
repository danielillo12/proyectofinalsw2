from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import cuenta
from .form import registros,logins
# Create your views here.
def index(request):
	nombre_user=''
	template = loader.get_template('index.html')
	lista = cuenta.objects.all()
	Forma=logins(request.POST or None)
	context = {
		#'lista_cuenta':lista,
		'forma':Forma
	}
	if Forma.is_valid():
		datos=Forma.cleaned_data
		nombre_user=datos.get("nombre")
		clave_user=datos.get("clave")
		print(nombre_user)

	for abc in lista:
		if abc.nombre==nombre_user and abc.clave == clave_user or abc.numero==nombre_user and abc.clave==clave_user:
			print(nombre_user)
			return redirect('https://google.com')
		#else:
		#	mensaje ="<center><br><br><br><br><h1>Datos mal ingresados</h1></br></br></br></br>"
		#	return HttpResponse(mensaje)


	return HttpResponse(template.render(context, request))
	
def registro(request):
	template = loader.get_template('registro.html')
	lista = cuenta.objects.all()
	forma=registros(request.POST or None)
	if forma.is_valid():
		datos = forma.cleaned_data
		nombre_user=datos.get("nombre")
		clave_user=datos.get("clave")
		telefono_user=datos.get("telefono")
		print (nombre_user)
		print (clave_user)
		print (telefono_user)
		bolean = True 
		for abc in lista:
			if abc.nombre==nombre_user or abc.numero==telefono_user:
				bolean=False

		if bolean == True:

			db_registro=cuenta(nombre=nombre_user,clave=clave_user,numero=telefono_user)
			db_registro.save()
			return HttpResponseRedirect('http://127.0.0.1:8000') 
		else:
			mensaje ="<center><br><br><br><br><h1>Ya existe ese usuario/numero </h1></br></br></br></br>"
			return HttpResponse(mensaje)
	context = {}
	return HttpResponse(template.render({'forma':forma}, request))