from django import forms

from reservas.models import Room
from tour_package.models import Tour_Package

class RoomForm(forms.ModelForm):

	class Meta:
		model = Room

		fields = "__all__"

		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'calificacion': forms.NumberInput(attrs={'class':'form-control'}),
			'path_image':forms.FileInput(attrs={'class':'form-control'}),
			'num_camas': forms.NumberInput(attrs={'class':'form-control'}),
			'num_adultos': forms.NumberInput(attrs={'class':'form-control'}),
			'num_ninos': forms.NumberInput(attrs={'class':'form-control'}),
			'precio':forms.NumberInput(attrs={'class':'form-control'}),
		}

class TourForm(forms.ModelForm):

	class Meta:
		model = Tour_Package

		fields = [
			'titulo',
			'descripcion',
			'precio',
		]

		labels = {
			'titulo':'Titulo del Paquete',
			'descripcion':'Descripcion del Paquete',
			'precio':'Precio del Paquete',
		}

		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'precio':forms.NumberInput(attrs={'class':'form-control'}),
		}