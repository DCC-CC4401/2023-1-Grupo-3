from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario

def login(request):
    credenciales = Usuario.objects.all()

    if request.method == "GET":
        print("Se registro")
        return HttpResponse()
    
    if request.method == "POST":
        print("Se loggeo")
        return HttpResponse()