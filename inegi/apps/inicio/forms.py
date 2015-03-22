from django import forms

#FORMULARIO UPDATE
class Update(forms.Form):
	archivo = forms.FileField(label='Agregar archivo')

class Windows(forms.Form):
	windows = forms.FileField(label = 'Agregar archivo Windows')