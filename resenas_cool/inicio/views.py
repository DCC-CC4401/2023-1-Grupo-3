from django.shortcuts import render, redirect
from resenas.models import Resenas, Categorias
from usuarios.models import Usuario

 
def ver_resenas(request):
    if request.method == 'GET':
        return render(request, 'inicio/inicio.html', {"user": request.user ,"categorias": Categorias.objects.all(), "resenas": Resenas.objects.all()})