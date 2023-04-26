from django.db import models
from django.utils import timezone
#from categorias.models import Categoria

class Usuario(models.Model):  
    id = models.AutoField(primary_key=True)  
    user_name = models.CharField(max_length=25) 
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    
    #categoria = models.ForeignKey(Categoria, default="general", on_delete=models.CASCADE)  # la llave foránea

    def __str__(self):
        return self.user_name # name to be shown when called

