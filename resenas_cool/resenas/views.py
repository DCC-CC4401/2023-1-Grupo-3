from django.shortcuts import render, redirect
from resenas.forms import NuevaResenaModelForm
from resenas.models import Resenas, Categorias
from usuarios.models import Usuario


def nueva_resena(request):
  
  if request.user.is_authenticated:
   form_resena = NuevaResenaModelForm()
   categorias =Categorias.objects.all()
   
   if request.method == "GET":
      print(request.user)
      return render(request, "../templates/nu_resena.html", {"form_resena": form_resena, "categorias":categorias})
   
   elif request.method == "POST":  
         
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
         
         nueva_resena = Resenas(nombre_producto=nombre_producto, titulo=titulo, descripcion=descripcion, id_categoria=categoria, id_usuario=request.user)
         # if nueva_resena.is_valid():
         nueva_resena.save()

         resena = Resenas.objects.get(nombre_producto=nombre_producto, titulo=titulo, descripcion=descripcion, id_categoria=categoria, id_usuario=request.user)
         return redirect('mostrar_resena', review_id=resena.id)

         # categorias =Categorias.objects.all()
         # return render(request, "../templates/nu_resena.html", {"form_resena": form_resena, "categorias":categorias})
   
   else:
      return redirect('login')

def mostrar_resena(request, review_id):
   
   resena = Resenas.objects.get(id=review_id)
   user = request.user
   return render(request, '../templates/mostrar_resena.html', {"resena": resena, "user": user})


def borrar(request, review_id):
   review = Resenas.objects.get(id=review_id)
   review.delete()
   return redirect('nueva_resena')

def modificar_resena(request, review_id):
   resena = Resenas.objects.get(id=review_id)

   categorias =Categorias.objects.all()
   
   if request.method == "GET":
      return render(request, "../templates/mod_resena.html", {"resena": resena, "categorias":categorias})
   
   elif request.method == "POST":
      resena.nombre_producto = request.POST["nombre_producto"]
      resena.titulo = request.POST["titulo"] 
      nombre_categoria = request.POST["selector_categoria"]  
      resena.id_categoria = Categorias.objects.get(nombre=nombre_categoria)
      resena.descripcion = request.POST["descripcion"]
      
      resena.save()
      return redirect('mostrar_resena', review_id=review_id)
   






