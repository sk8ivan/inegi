from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView,CreateView
from .forms import Update, Windows

# Create your views here.
class Inicio(TemplateView):
	template_name = 'inicio.html'
	model = Update
	context_object_name = 'Update'

class Exito(TemplateView):
	template_name = 'exito.html'

class Configuracion(TemplateView):
	template_name = 'menu.html'

#
def AltaUpdate(request):
	
	if request.method == 'POST':
		form = Update(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/exito.html/')
	

	else:
		form = Update()
		print("Entrando al formulario")

	return render(request, 'update.html', {'form':form})

def AltaWindows(request):
	
	if request.method == 'POST':
		form = Windows(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/exito.html/')
	

	else:
		form = Windows()

	return render(request, 'windows.html', {'form':form})


