from django.shortcuts import render, redirect

from todoapp.models import Tarea
from categorias.models import Categoria

def tareas(request):
    mis_tareas = Tarea.objects.all()
    categorias = Categoria.objects.all()

    if request.method == "GET":
        return render(request, "todoapp/index.html", {"tareas": mis_tareas, "categorias": categorias})

    if request.method == "POST":  # revisar si el método de la request es POST
        if "taskAdd" in request.POST:  # verificar si la request es para agregar una tarea (esto está definido en el button)
            titulo = request.POST["titulo"]  # titulo de la tarea
            
            nombre_categoria = request.POST["selector_categoria"]  # nombre de la categoria
            categoria = Categoria.objects.get(nombre=nombre_categoria)  # buscar la categoría en la base de datos
            
            contenido = request.POST["contenido"]  # contenido de la tarea
            
            nueva_tarea = Tarea(titulo=titulo, contenido=contenido, categoria=categoria)  # Crear la tarea
            nueva_tarea.save()  # guardar la tarea en la base de datos.

            return redirect("/tareas")  # recargar la página.

