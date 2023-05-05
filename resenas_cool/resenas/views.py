from django.shortcuts import render, redirect
from resenas.forms import NuevaResenaModelForm
from resenas.models import Resenas, Categorias


def nueva_resena(request):
  
  if request.method == "GET":
     form_resena = NuevaResenaModelForm()
     return render(request, "../templates/nueva_resena.html", {"form_resena": form_resena})
  
  if request.method == "POST":  
     if "reviewAdd" in request.POST:  #crear boton
        nombre_producto = request.POST["nombre_producto"]
        titulo = request.POST["titulo"] 
        nombre_categoria = request.POST["selector_categoria"]  
        categoria = Categorias.objects.get(nombre=nombre_categoria)
        descripcion = request.POST["descripcion"]
        foto = request.POST["foto"]
        
        nueva_resena = Resenas(nombre_producto=nombre_producto, titulo=titulo, descripcion=descripcion, id_categoria=categoria.id, id_usuario=request.user, foto=foto)
        if nueva_resena.is_valid():
           nueva_resena.save()
           
        return redirect('/resenas')
