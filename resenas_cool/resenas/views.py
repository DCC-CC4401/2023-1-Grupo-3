from django.shortcuts import render, redirect
from resenas.forms import NuevaResenaModelForm
from resenas.models import Resenas, Categorias
from usuarios.models import Usuario
from django.contrib import messages
from django.http import HttpResponseRedirect



def nueva_resena(request):
  
  if request.user.is_authenticated:
   form_resena = NuevaResenaModelForm()
   categorias = Categorias.objects.all()
   
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
         foto = request.POST["foto"]
         
         nueva_resena = Resenas(nombre_producto=nombre_producto, titulo=titulo, descripcion=descripcion, id_categoria=categoria, id_usuario=request.user, foto=foto)
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
   resena = Resenas.objects.get(id=review_id)
   if(request.user != resena.id_usuario):
      return redirect("nueva_resena")
   
   else:
      review = Resenas.objects.get(id=review_id)
      review.delete()
      return redirect('nueva_resena')

def modificar_resena(request, review_id):

   resena = Resenas.objects.get(id=review_id)

   if(request.user != resena.id_usuario):
      return redirect("nueva_resena")
   

   else:

      # resena_ognl = resena
      categorias = Categorias.objects.all()

      if request.method == 'POST':
         form = NuevaResenaModelForm(request.POST, instance=resena)
         if form.is_valid():
               form.save()
         return redirect('mostrar_resena', review_id=review_id)
      
      else:
         form = NuevaResenaModelForm(instance=resena)

      return render(request, '../templates/nueva_resena.html', {'form': form, 'resena':resena, 'categorias':categorias})

# def cancelar(request, review_id):
#    redirect('mostrar_resena', review_id=review_id)






