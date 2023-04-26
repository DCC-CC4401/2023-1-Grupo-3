from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from usuarios.login import NuevaTareaForm

def login(request):
    credenciales = Usuario.objects.all()

    if request.method == "GET":
        return render(request, "usuarios/login.html", {"credenciales": credenciales, "form_login": NuevaTareaForm()})
    
    if request.method == "POST":
        return "Not implemented yet"