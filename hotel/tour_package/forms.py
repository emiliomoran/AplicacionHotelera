from django import forms

from tour_package.models import Tour_Package

class TourForm(forms.ModelForm):

	class Meta:
		model = Tour_Package

		fields = [
			'title',
			'description',
			'company',
			'days',
			'hours',
			'price',
			'path_image',
		]

		labels = {
			'title':'Titulo del Paquete',
			'description':'Descripcion del Paquete',
			'company':'Compañia',
			'days':'Dias del Tour',
			'hours':'Horas del Tour',
			'price':'Precio del Paquete',
			'path_image':'Subir Imagen',
		}

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control'}),
			'description': forms.TextInput(attrs={'class':'form-control'}),
			'company':forms.TextInput(attrs={'class':'form.control'}),
			'days':forms.TextInput(attrs={'class':'form-control'}),
			'hours':forms.TextInput(attrs={'class':'form-control'}),
			'price':forms.NumberInput(attrs={'class':'form-control'}),
			'path_image':forms.FileInput(attrs={'class':'form-control'}),

		}