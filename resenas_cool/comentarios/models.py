from django.db import models

from usuarios.models import Usuario
from resenas.models import Resenas


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    id_resena = models.ForeignKey(Resenas, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.id 
