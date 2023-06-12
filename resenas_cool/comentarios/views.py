from django.shortcuts import render, redirect
from comentarios.forms import NuevoComentarioModelForm
from comentarios.models import Comentario
from resenas.models import Resenas 


# Create your views here.

def nuevo_comentario(request, review_id):
    #solo un usuario registrado puede agregar comentarios
    if request.user.is_authenticated:
        form_comentario = NuevoComentarioModelForm()
        if request.method == "GET":
          return render(request, "../templates/nuevo_comentario.html",{"form_comentario": form_comentario})
        elif request.method == "POST":
          descripcion = request.POST['descripcion']
          #obtenemos el id de la reseña
          resena = Resenas.objects.get(id=review_id)
          nuevo_comentario = Comentario(descripcion=descripcion,id_usuario = request.user,id_resena=resena)
          nuevo_comentario.save()
          comentario = Comentario.objects
          #redireccionalo hacia la misma página que contenga todos los comentarios(?)
          return redirect('mostrar_resena',review_id=review_id)
    else:   # Si el usuario no esta logeado
        return redirect('inicio')    # Redireccionamos donde mismo
    

def borrar_comentario(request, id, id_resena):
  comentario = Comentario.objects.get(id=id)
  if (request.user != comentario.id_usuario):
        # Redireccionamos a nueva_resena
        return redirect("mostrar_resena",review_id = id_resena)
    # Si el usuario es el que hizo la reseña
  else:
      # La borramos
      comentario.delete()
      # Redireccionamos a nueva_reseña
      return redirect("mostrar_resena",review_id = id_resena)