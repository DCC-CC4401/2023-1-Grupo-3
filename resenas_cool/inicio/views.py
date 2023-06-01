from django.shortcuts import render, redirect
from resenas.models import Resenas, Categorias, Valoracion
from usuarios.models import Usuario

# Definimos funcion para mostrar las reseñas
def ver_resenas(request):
    if request.method == 'GET':
        # Le pasamos para completar su usuario, categorias para llenar la navbar y resenas para que obtenga de la BD
        return render(request, 'inicio/inicio.html', {"user": request.user ,"categorias": Categorias.objects.all(), "resenas": Resenas.objects.all(), "valoraciones": Valoracion.objects.all()})
        