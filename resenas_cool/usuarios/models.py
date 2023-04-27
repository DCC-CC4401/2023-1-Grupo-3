from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
#from categorias.models import Categoria

class Usuario(AbstractUser):  
    id = models.AutoField(primary_key=True)  
    user_name = models.CharField(max_length=25) 
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user_name # name to be shown when called

