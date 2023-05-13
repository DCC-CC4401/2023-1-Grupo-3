from django import forms
from resenas.models import Resenas, Categorias

class NuevaResenaModelForm(forms.ModelForm):
   nombre_producto = forms.CharField(label="Nombre Producto")
   titulo = forms.CharField(label="Título de la Reseña")
   categoria = forms.ModelChoiceField(queryset=Categorias.objects.all())
   descripcion = forms.CharField(widget=forms.Textarea()) 
   #foto = forms.ImageField()   

   class Meta:
      model = Resenas
      fields = ['nombre_producto', 'titulo', 'categoria', 'descripcion'] #le saque foto
   
   def clean_nombre_producto(self):
      field = self.cleaned_data.get("nombre_producto")
      if not field:
         raise forms.ValidationError("Debe agregar nombre del producto")
      ##no se si hay que agregar otras condiciones
      return field
   
   def clean_titulo(self):
      field = self.cleaned_data.get("titulo")
      if not field:
         raise forms.ValidationError("Debe agregar titulo de la reseña")
      elif len(field)>25:
         raise forms.ValidationError("El titulo puede contener maximo 25 caracteres")
   
      ## lo mismo de arriba
      ## en volá pedir que tenga letras(?) onda con una expresion regular o algo así
      return field
   
   #hay que validar que elija una categoria pero no sé cómo
   
   def clean_descripción(self):
      field = self.cleaned_data.get("descripcion")
      if not field:
         raise forms.ValidationError("Debe agregar nombre del producto")
      elif len(field) < 5: # no sé si deberiamos poner largo minimo asi que si quieren lo sacan  
         raise forms.ValidationError("La descripción debe contener mínimo 5 caracteres")
      return field
   
   def clean_foto(self):
      field = self.cleaned_data.get("nombre_producto")
      if not field:
         raise forms.ValidationError("Debe agregar foto/s")
      ## no sé si esto se hace así sjkd
      return field