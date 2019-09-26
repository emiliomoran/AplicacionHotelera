from django import forms

from tour_package.models import Tour_Package

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