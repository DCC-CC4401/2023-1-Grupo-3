from django.shortcuts import render, redirect
from resenas.forms import NuevaResenaModelForm
from resenas.models import Resenas, Categorias
from usuarios.models import Usuario


def nueva_resena(request):
  
  #agregar if is_authenticated
  #si no, redirigir a login
  form_resena = NuevaResenaModelForm()
  categorias =Categorias.objects.all()
     
  
  if request.method == "GET":
     print(request.user)
     return render(request, "../templates/nu_resena.html", {"form_resena": form_resena, "categorias":categorias})
  
  if request.method == "POST":  
      
      # form_resena = NuevaResenaModelForm(request.POST)
      # if form_resena.is_valid():
      #    form_resena.save()

       #if "reviewAdd" in request.POST:  #crear boton
      nombre_producto = request.POST["nombre_producto"]
      titulo = request.POST["titulo"] 
      nombre_categoria = request.POST["selector_categoria"]  
      categoria = Categorias.objects.get(nombre=nombre_categoria)
      descripcion = request.POST["descripcion"]
      #foto = request.POST["foto"]
      usuario = Usuario.objects.get(username="valer")
        
      
      nueva_resena = Resenas(nombre_producto=nombre_producto, titulo=titulo, descripcion=descripcion, id_categoria=categoria, id_usuario=usuario)
      #if nueva_resena.is_valid():
      nueva_resena.save()

      resena = Resenas.objects.get(nombre_producto=nombre_producto, titulo=titulo, descripcion=descripcion, id_categoria=categoria, id_usuario=usuario)
      return redirect('mostrar_resena', review_id=resena.id)

      # categorias =Categorias.objects.all()
      return render(request, "../templates/nu_resena.html", {"form_resena": form_resena, "categorias":categorias})
  

def mostrar_resena(request, review_id):
   
   resena = Resenas.objects.get(id=review_id)
   return render(request, '../templates/mostrar_resena.html', {"resena": resena})

