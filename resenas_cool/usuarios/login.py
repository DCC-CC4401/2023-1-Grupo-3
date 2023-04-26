from django import forms


class NuevaTareaForm(forms.Form):
   nombre = forms.CharField(max_length=25, required=True)
   contraseña = forms.CharField(max_length=25, required=True, widget=forms.PasswordInput())
