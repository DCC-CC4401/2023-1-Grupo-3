from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from usuarios.models import Usuario
from usuarios.login import LoginForm
from usuarios.register import RegisterForm
from django.contrib import messages

def login(request):
    credenciales = Usuario.objects.all()

    if request.method == "GET":
        return render(request, "usuarios/login.html", {"credenciales": credenciales, "form_login": LoginForm()})
    
    if request.method == "POST":
        username = request.POST["nombre"]
        password = request.POST["contraseña"]

        if Usuario.objects.filter(username=username, password=password).exists():
            print("Usuario encontrado")
            return HttpResponseRedirect("nueva_resena")
        
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
            return HttpResponseRedirect("login")
    
def register(request):
    credenciales = Usuario.objects.all()
    if request.method == "GET":
        return render(request, "usuarios/register.html", {"credenciales": credenciales, "form_register": RegisterForm()})
    if request.method == "POST":
        username = request.POST["nombre"]
        password = request.POST["contraseña"]

        # Checkeo de largo
        if len(username) < 5:
            messages.error(request, "Nombre de usuario demasiado corto, debe ser a lo menos 5")
            return HttpResponseRedirect("login")

        usuario = Usuario.objects.create(username=username, password=password)
        return HttpResponseRedirect("login")    