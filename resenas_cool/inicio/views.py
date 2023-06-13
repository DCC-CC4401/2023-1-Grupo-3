from django.shortcuts import render, redirect
from resenas.models import Resenas, Categorias
from usuarios.models import Usuario
from django.contrib.auth import logout


# Definimos funcion para mostrar las reseñas
def ver_resenas(request, categoria=None, usuario=None):
    if request.method == 'GET':
        resenas = Resenas.objects.all()
        error = None
        if request.GET.get("usuario"):
            usuario=request.GET.get("usuario")
        if categoria != None:
            # Si se pasa una categoria, filtramos las reseñas por categoria
            categoria = Categorias.objects.get(nombre=categoria)

            resenas = resenas.filter(id_categoria=categoria)
        if usuario != None:
            # Si se pasa un usuario, filtramos las reseñas por usuario
            try:
                usuario = Usuario.objects.get(username=usuario)

                resenas = resenas.filter(id_usuario=usuario)
            except Usuario.DoesNotExist:
                error = "Usuario no encontrado"
                resenas = []

        # Le pasamos para completar su usuario, categorias para llenar la navbar y resenas para que obtenga de la BD
        return render(request, 'inicio/inicio.html', {"user": request.user, "categorias": Categorias.objects.all(), "resenas": resenas, "categoria": categoria, "usuario": usuario, "error": error})


def logout_view(request):
    logout(request)
    return redirect('ver_resenas')