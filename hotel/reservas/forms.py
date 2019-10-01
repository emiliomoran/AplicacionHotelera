from django import forms

from reservas.models import Room

class RoomForm(forms.ModelForm):

	class Meta:
		model = Room

		fields = "__all__"

		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'calificacion': forms.NumberInput(attrs={'class':'form-control'}),
			'path_image':forms.TextInput(attrs={'class':'form-contro'}),
			'num_camas': forms.NumberInput(attrs={'class':'form-control'}),
			'num_adultos': forms.NumberInput(attrs={'class':'form-control'}),
			'num_ninos': forms.NumberInput(attrs={'class':'form-control'}),
			'precio':forms.NumberInput(attrs={'class':'form-control'}),
		}