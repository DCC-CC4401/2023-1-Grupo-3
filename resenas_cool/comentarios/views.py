from django.shortcuts import render, redirect
from comentarios.forms import NuevoComentarioModelForm
from comentarios.models import Comentario



# Create your views here.

def nuevo_comentario(request):
    #solo un usuario registrado puede agregar comentarios
    if request.user.is_authenticated:
        form_comentario = NuevoComentarioModelForm()
        if request.method == "GET":
          #no sé pa donde mandarlo D:, pa la pagina de las reseñas del producto (?)
          return render(request, "../templates/nuevo_comentario.html",{"form_comentario": form_comentario})
        elif request.method == "POST":
          descripcion = request.POST['descripcion']
          nuevo_comentario = Comentario(descripcion=descripcion,id_usuario = request.user)
          nuevo_comentario.save()
          comentario = Comentario.objects
          #redireccionalo hacia la misma página que contenga todos los comentarios(?)
          return redirect('inicio')
    else:   # Si el usuario no esta logeado
        return redirect('inicio')    # Redireccionamos donde mismo