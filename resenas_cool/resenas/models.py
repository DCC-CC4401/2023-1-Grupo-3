from django.db import models
from django.utils import timezone
from usuarios.models import Usuario

# Creamos clase categoría
class Categorias(models.Model):
    # No pueden existir 2 categorías con el mismo nombre
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=25, unique=True)
    
    def __str__(self):
        return self.nombre # name to be shown when called
    
# Creamos clase reseñas
class Resenas(models.Model):
    # Se crean los campos del modelo para crear una nueva reseña
    id = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=25)
    fecha_creación = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    titulo = models.CharField(max_length=25)
    descripcion = models.TextField(blank=True)

    id_categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    likes = models.IntegerField(default=0)

    foto = models.ImageField(upload_to='media/images/resenas',  blank=True, null=True)

    def __str__(self):
        return self.titulo  # name to be shown when called

# Creamos clase valoracion
class Valoracion(models.Model):
    # id
    id = models.AutoField(primary_key=True)
    # id reseña
    id_res = models.ForeignKey(Resenas, on_delete=models.CASCADE)
    # id usuario
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)