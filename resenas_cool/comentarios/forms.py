from django import forms
from comentarios.models import Comentario

class NuevoComentarioModelForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Comentario
        fields = ['descripcion']
    
        