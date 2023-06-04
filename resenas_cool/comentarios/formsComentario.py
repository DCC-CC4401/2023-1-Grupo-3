from django import forms
from models import Comentario

class NuevoComentarioModelForm(forms.ModelForm):
    descripcion = forms.ChardField(widget=forms.Textarea())

    class Meta:
        model = Comentario
        fields = ['descripcion']
    
        