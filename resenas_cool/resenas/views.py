from django.shortcuts import render, redirect
from resenas.forms import NuevaResenaModelForm
from comentarios.models import Comentario
from resenas.models import Resenas, Categorias, Valoracion
from usuarios.models import Usuario
from comentarios.models import Comentario
from django.contrib import messages
from django.http import HttpResponseRedirect

# Definimos una función para crear una nueva reseña
def nueva_resena(request):
    # Si el usuario esta logeado
    if request.user.is_authenticated:
        form_resena = NuevaResenaModelForm()    # Obtenemos el formulario para la reseña
        categorias = Categorias.objects.all()   # Obtenemos las categorías para mostrarlas en el select

        if request.method == "GET": # Si se ingresa a la página antes de rellenar los datos
            # Render al formulario de nueva reseña agregando las categorías
            return render(request, "../templates/nu_resena.html", {"form_resena": form_resena, "categorias": categorias})

        elif request.method == "POST":  # Si se ingresa luego de apretado el botón
            # Guardamos los datos ingresados
            nombre_producto = request.POST["nombre_producto"]
            titulo = request.POST["titulo"]
            nombre_categoria = request.POST["selector_categoria"]
            categoria = Categorias.objects.get(nombre=nombre_categoria)
            descripcion = request.POST["descripcion"]
            foto = request.FILES["foto"]
            # Creamos un objeto reseña y le asignamos las variables correspondientes
            nueva_resena = Resenas(nombre_producto=nombre_producto, titulo=titulo,
                                    descripcion=descripcion, id_categoria=categoria, id_usuario=request.user, foto=foto)
            # if nueva_resena.is_valid():
            nueva_resena.save() # Guardamos en la BD el objeto
            resena = Resenas.objects.get(nombre_producto=nombre_producto, titulo=titulo,
                                            descripcion=descripcion, id_categoria=categoria, id_usuario=request.user)
            # Redireccionamos a mostrar_resena
            return redirect('mostrar_resena', review_id=resena.id)
    else:   # Si el usuario no esta logeado
        return redirect('login')    # Redireccionamos donde mismo

# Definimos la función mostrar reseña
def mostrar_resena(request, review_id):
    # Obtenemos el objeto reseña
    resena = Resenas.objects.get(id=review_id)
    # Obtenemos el usuario
    user = request.user
    print(user)
    # Obtenemos la cantidad de resenas
    resena.likes = Valoracion.objects.filter(id_res=review_id).count()
    liked = False
    if user.is_authenticated:
        liked = Valoracion.objects.filter(id_usuario=user, id_res=resena).count() != 0
    # Obtenemos los comentarios
    comentarios = Comentario.objects.filter(id_resena=review_id)
    # Creamos una tupla con autor y comentario
    autor_comentario = [(Usuario.objects.get(id=i.id_usuario_id), i.descripcion, i.id) for i in comentarios]
    # Vemos si esta logeado
    auth = user.is_authenticated

    # Botón
    if request.method == 'POST':
        # no esta logeado
        if not user.is_authenticated:
            return redirect('register')
        # Vemos si el usuario ya dio like
        if liked == False:
            nueva_valoracion = Valoracion(id_usuario=user, id_res=resena)
            nueva_valoracion.save()
            liked = True
        elif liked == True:
            val = Valoracion.objects.filter(id_usuario=user, id_res=resena)
            val.delete()
            liked = False
        resena.likes = Valoracion.objects.filter(id_res=review_id).count()   
    # Render al template con resena y usuario
    return render(request, '../templates/mostrar_resena.html', {"resena": resena, "user": user, "liked": liked, "autor_comentario": autor_comentario, "auth": auth})



# Definimos la función de borrar reseña
def borrar(request, review_id):
    # Obtenemos el objeto reseña
    resena = Resenas.objects.get(id=review_id)
    # Si el usuario es distinto al que hizo la reseña
    if (request.user != resena.id_usuario):
        # Redireccionamos a nueva_resena
        return redirect("nueva_resena")
    # Si el usuario es el que hizo la reseña
    else:
        # Obtenemos la review
        review = Resenas.objects.get(id=review_id)
        # La borramos
        review.delete()
        # Redireccionamos a nueva_reseña
        return redirect('ver_resenas')


# Definimos la función de modificar reseña
def modificar_resena(request, review_id):
    # Obtenemos la reseña
    resena = Resenas.objects.get(id=review_id)
    # Si el usuario es diferente al que hizo la reseña
    if (request.user != resena.id_usuario):
        # No lo puede modificar, redireccionamos a nueva_reseña
        return redirect("nueva_resena")
    # Si el usuario es el que es hizo la reseña
    else:
        # Obtenemos las categorías
        categorias = Categorias.objects.all()
        # Si se ingresa luego de apretado el botón
        if request.method == 'POST':
            nuevo_nombre_producto = request.POST.get('nombre_producto')
            nuevo_titulo = request.POST.get('titulo')
            nombre_categoria = request.POST["selector_categoria"]
            nueva_categoria = Categorias.objects.get(nombre=nombre_categoria)
            nueva_descripcion = request.POST.get('descripcion')
            nueva_foto = request.FILES.get('foto')

            # Actualizar los campos de la instancia de la reseña
            resena.nombre_producto = nuevo_nombre_producto if nuevo_nombre_producto is not None else resena.nombre_producto 
            print(nuevo_nombre_producto)
            print(nueva_foto)
            resena.titulo = nuevo_titulo if nuevo_titulo is not None else resena.titulo
            resena.id_categoria = nueva_categoria if nueva_categoria is not None else resena.id_categoria
            resena.descripcion = nueva_descripcion if nueva_descripcion is not None else resena.descripcion
            resena.foto = nueva_foto if nueva_foto is not None else resena.foto

            # Guardar los cambios en la base de datos
            resena.save()

            # Redireccionamos a mostrar reseña
            return redirect('mostrar_resena', review_id=review_id)

        else: # Si se ingresa a la página antes de rellenar los datos
            form = NuevaResenaModelForm(instance=resena)
        # Render de nueva reseña con sus parámetros correspondientes
        return render(request, '../templates/mod_resena.html', {'form': form, 'resena': resena, 'categorias': categorias})
