from django import forms

from reservas.models import Room, RoomType, Document
from tour_package.models import Tour_Package

class RoomForm(forms.ModelForm):

	class Meta:
		model = Room

		fields = "__all__"

		# field_test = forms.ModelChoiceField(queryset=RoomType.objects.all(), to_field_name="id", empty_label=None)

		widgets = {
			# 'codigo': forms.TextInput(attrs={'class':'form-control'}),			
			#'titulo': forms.TextInput(attrs={'class':'form-control'}),
			# 'id_roomtype': form.ModelChoiceField(queryset=RoomType.objects.all(), to_field_name="id"),
			'id_roomtype': forms.Select(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'numero': forms.NumberInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'calificacion': forms.HiddenInput(attrs={'class':'form-control'}),
			# 'path_image':forms.FileInput(attrs={'class':'form-control'}),
			#'path_image':forms.TextInput(attrs={'class':'form-control'}),
			'num_camas': forms.NumberInput(attrs={'class':'form-control'}),
			'num_adultos': forms.NumberInput(attrs={'class':'form-control'}),
			'num_ninos': forms.NumberInput(attrs={'class':'form-control'}),
			'precio':forms.NumberInput(attrs={'class':'form-control'}),
			'disponible': forms.HiddenInput(attrs={'class':'form-control'}),		
			'eliminado': forms.HiddenInput(attrs={'class':'form-control'}),
		}

class TourForm(forms.ModelForm):

	class Meta:
		model = Tour_Package

		fields = [
			'title',
			'description',
			'price',
			'path_image',
		]

		labels = {
			'title':'Titulo del Paquete',
			'description':'Descripcion del Paquete',
			'price':'Precio del Paquete',
			'path_image':'Url de la Imagen',
		}

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control'}),
			'description': forms.TextInput(attrs={'class':'form-control'}),
			'price':forms.NumberInput(attrs={'class':'form-control'}),
			'path_image':forms.TextInput(attrs={'class':'form-control'}),
		}

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ('description', 'document', )