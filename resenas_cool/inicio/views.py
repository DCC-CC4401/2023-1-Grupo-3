from django.shortcuts import render
from resenas.models import Resenas, Categorias

 
def ver_resenas(request):
    if request.method == 'GET':
        return render(request, 'inicio/inicio.html', {"categorias": Categorias.objects.all(), "resenas": Resenas.objects.all()})