from django.shortcuts import render, redirect
from resenas.forms import NuevaResenaModelForm
from resenas.models import Resenas, Categorias


def nueva_resena(request):
  
  #agregar if is_authenticated
  #si no, redirigir a login
  
  if request.method == "GET":
     form_resena = NuevaResenaModelForm()
     categorias =Categorias.objects.all()
     return render(request, "../templates/nu_resena.html", {"form_resena": form_resena, "categorias":categorias})
  
  if request.method == "POST":  
      
      form_resena = NuevaResenaModelForm(request.POST)
      #if form_resena.is_valid():
      #   form_resena.save()

       #if "reviewAdd" in request.POST:  #crear boton
      nombre_producto = request.POST["nombre_producto"]
      titulo = request.POST["titulo"] 
      nombre_categoria = request.POST["selector_categoria"]  
      categoria = Categorias.objects.get(nombre=nombre_categoria)
      descripcion = request.POST["descripcion"]
      #foto = request.POST["foto"]
        
      nueva_resena = Resenas(nombre_producto=nombre_producto, titulo=titulo, descripcion=descripcion, id_categoria=categoria, id_usuario=request.user)
      #if nueva_resena.is_valid():
      nueva_resena.save()

      categorias =Categorias.objects.all()#hay que sacarlo cuando cambiemos el render   
      return render(request, "../templates/nu_resena.html", {"form_resena": form_resena, "categorias":categorias})
