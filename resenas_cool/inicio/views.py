from django.shortcuts import render, redirect
from resenas.models import Resenas, Categorias, Valoracion
from usuarios.models import Usuario

# Definimos funcion para mostrar las reseñas
def ver_resenas(request):
    if request.method == 'GET':
        resenas = Resenas.objects.all()
        valoraciones = Valoracion.objects.all()
        # Calculamos la cantidad de likes de cada uno
        r_v = [0] * len(resenas)
        for i in resenas:
            for j in valoraciones:
                if i.id == j.id_res.id:
                    r_v[i.id] += 1
        # Le pasamos para completar su usuario, categorias para llenar la navbar y resenas para que obtenga de la BD
        return render(request, 'inicio/inicio.html', {"user": request.user ,"categorias": Categorias.objects.all(), "resenas": resenas, "r_v": r_v})
        