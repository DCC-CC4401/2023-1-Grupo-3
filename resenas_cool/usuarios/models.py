from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
#from categorias.models import Categoria

class Usuario(AbstractUser):  
    #todo se hereda de AbstractUser
    #id = models.AutoField(primary_key=True)  
    #username = models.CharField(max_length=25, unique=True) 
    #password = models.CharField(max_length=25)
    #email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username # name to be shown when called

