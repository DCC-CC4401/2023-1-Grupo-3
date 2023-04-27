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
        user_name = request.POST["nombre"]
        password = request.POST["contraseña"]

        if Usuario.objects.filter(user_name=user_name, password=password).exists():
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
        user_name = request.POST["nombre"]
        password = request.POST["contraseña"]

        usuario = Usuario.objects.create(user_name=user_name, password=password)
        return HttpResponseRedirect("login")    