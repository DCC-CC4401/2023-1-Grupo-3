from django.shortcuts import render
from resenas.models import Resena


def ver_resenas(request):
    if request.method == 'GET':
        return render(request, 'ver_resenas.html', {"resenas": Resena.objects.all()})