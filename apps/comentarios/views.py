from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import DeleteView, UpdateView
from apps.publicaciones.models import Publicacion
from .models import Comentario
from django.urls import reverse_lazy
from .forms import Form_Modificacion

def Agregar_Comentario(request,pk):

	texto = request.POST.get('comentario',None)

	publicacion = Publicacion.objects.get(pk = pk)
	usuario = request.user
	Comentario.objects.create(texto = texto, usuario = usuario, publicacion = publicacion)

	return HttpResponseRedirect(reverse_lazy('publicaciones:detalle_publicacion', kwargs = {'pk':pk}))

class BorrarComentario(DeleteView):
	model = Comentario
	def get_success_url(self):         
		return reverse_lazy('publicaciones:detalle_publicacion',kwargs={'pk': self.object.publicacion.pk})

class ModificaComentario(UpdateView):
	model = Comentario
	form_class = Form_Modificacion
	template_name = 'ver.html'
	def get_success_url(self):         
		return reverse_lazy('publicaciones:detalle_publicacion',kwargs={'pk': self.object.publicacion.pk})