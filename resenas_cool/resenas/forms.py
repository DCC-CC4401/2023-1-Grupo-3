from django import forms
from resenas.models import Resenas, Categorias

class NuevaResenaForm(forms.Form):
   nombre_producto = forms.CharField(label="Nombre Producto")
   titulo = forms.CharField(label="Título de la Reseña")
   categoria = forms.ModelChoiceField(queryset=Categorias.objects.all())
   descripcion = forms.CharField(widget=forms.Textarea()) 
   foto = forms.ImageField() #revisar   