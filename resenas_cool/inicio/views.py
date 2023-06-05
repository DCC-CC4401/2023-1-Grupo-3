from django.shortcuts import render, redirect
from resenas.models import Resenas, Categorias
from usuarios.models import Usuario


# Definimos funcion para mostrar las reseñas
def ver_resenas(request, categoria=None, usuario=None):
    if request.method == 'GET':
        resenas = Resenas.objects.all()
        if categoria != None:
            # Si se pasa una categoria, filtramos las reseñas por categoria
            try:
                categoria = Categorias.objects.get(nombre=categoria)

                resenas = resenas.filter(id_categoria=categoria)
            except Categorias.DoesNotExist:
                pass
            except Resenas.DoesNotExist:
                pass
        if usuario != None:
            # Si se pasa un usuario, filtramos las reseñas por usuario
            usuario = Usuario.objects.get(username=usuario)

            resenas = resenas.filter(id_usuario=usuario)

        # Le pasamos para completar su usuario, categorias para llenar la navbar y resenas para que obtenga de la BD
        return render(request, 'inicio/inicio.html', {"user": request.user, "categorias": Categorias.objects.all(), "resenas": resenas})
