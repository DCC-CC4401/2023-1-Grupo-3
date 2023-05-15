from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from usuarios.models import Usuario
from usuarios.login import LoginForm
from usuarios.register import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm #add this


#cambiamos el nombre del metodo a ingreso, para que no haya ambiguedad con el login dentro
#del metodo
def ingreso(request):
    credenciales = Usuario.objects.all()

    if request.method == "GET":
        return render(request, "usuarios/login.html", {"credenciales": credenciales, "form_login": LoginForm()})
    
    if request.method == "POST":
        #form = AuthenticationForm(request, data=request.POST)
        #if form.is_valid():
        #    username = form.cleaned_data.get('username')
        #    password = form.cleaned_data.get('password')
        #    user = authenticate(username=username, password=password)
        #    if user is not None:
        #        login(request, user)
        #        messages.info(request, f"You are now logged in as {username}.")
        #        return redirect("main:homepage")
        #    else:
        #        messages.error(request,"Invalid username or password.")
        username = request.POST["nombre"]
        password = request.POST["contraseña"]
        user = authenticate(username=username, password=password) #busca al usuario en la BD
        if user is not None:   
            login(request,user) #método para que se quede "logeado"
            print("Usuario encontrado")
            return HttpResponseRedirect("ver_resenas")
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
        #cambiamos el metodo a create_user
        usuario = Usuario.objects.create_user(username=username, password=password)
        return HttpResponseRedirect("login")    