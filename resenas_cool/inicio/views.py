from django.shortcuts import render
from resenas.models import Resena, Categorias


def ver_resenas(request):
    if request.method == 'GET':
        return render(request, 'ver_resenas.html', {"categorias": Categorias.objects.all(), "resenas": Resena.objects.all()})