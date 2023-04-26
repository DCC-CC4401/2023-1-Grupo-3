from django import forms


class NuevaTareaForm(forms.Form):
   nombre = forms.CharField(max_length=25)
   contrasenna = forms.CharField(max_length=25)
