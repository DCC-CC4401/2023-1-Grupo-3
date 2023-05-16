from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Clase usuario
class Usuario(AbstractUser):  
    # Hereda de Abstract User
    
    def __str__(self):
        return self.username # name to be shown when called

