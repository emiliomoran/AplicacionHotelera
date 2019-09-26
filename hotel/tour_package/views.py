from django.shortcuts import render, get_object_or_404
from tour_package.models import Tour_Package
from django.views.generic import ListView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from tour_package.forms import TourForm

# Create your views here.



class TourList(ListView):
	
	model = Tour_Package
	context_object_name = 'tours'
	template_name = 'index_tours.html'

class TourCreate(CreateView):

	model = Tour_Package
	form_class = TourForm
	template_name = "tour_create_form.html"

	success_url = reverse_lazy("tour_package:tour_listar")

class TourEdit(UpdateView):

	model = Tour_Package
	context_object_name = 'tour'
	template_name = 'tour_edit.html'
	form_class = TourForm

	def get_object(self):
		id_ = self.kwargs.get("id_tour")
		return get_object_or_404(Tour_Package,id = id_)

	success_url = reverse_lazy("tour_package:tour_listar")

class TourEliminar(DeleteView):
	model = Tour_Package
	success_url = reverse_lazy("tour_package:tour_listar")

	def get_object(self):
		id_ = self.kwargs.get("id_tour")
		return get_object_or_404(Tour_Package,id = id_)

