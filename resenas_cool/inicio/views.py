from django.shortcuts import render, redirect
from resenas.models import Resenas, Categorias
from usuarios.models import Usuario

 
def ver_resenas(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            logged_in = True
        else:
            logged_in = False
        
        return render(request, 'inicio/inicio.html', {"user": Usuario.objects.all() ,"categorias": Categorias.objects.all(), "resenas": Resenas.objects.all()})