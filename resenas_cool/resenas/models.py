from django.db import models
from django.utils import timezone
from usuarios.models import Usuario

class Categorias(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=25, unique=True)
    
    #categoria = models.ForeignKey(Categoria, default="general", on_delete=models.CASCADE)  # la llave foránea

    def __str__(self):
        return self.nombre # name to be shown when called
    

class Resenas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=25)
    fecha_creación = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    titulo = models.CharField(max_length=25)
    descripcion = models.TextField(blank=True)

    id_categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    foto = models.ImageField(upload_to='media/images/resenas',  blank=True, null=True)

    def __str__(self):
        return self.titulo  # name to be shown when called
