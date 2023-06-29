from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from usuarios.models import Usuario
from usuarios.login import LoginForm
from usuarios.register import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Definimos la función de ingreso para no confundir con login
def ingreso(request):
    credenciales = Usuario.objects.all()

    if request.method == "GET": # Si se ingresa a la página antes de rellenar los datos
        # Render a la página con el formulario de login
        return render(request, "usuarios/login.html", {"credenciales": credenciales, "form_login": LoginForm()})
    
    if request.method == "POST": # Si se ingresa luego de apretado el botón
        # Obtenemos las credenciales ingresadas
        username = request.POST["nombre"]
        password = request.POST["contraseña"]
        user = authenticate(username=username, password=password) # Busca al usuario en la BD
        # Si encuentra al usuario
        if user is not None:
            login(request,user) # Método para que se quede "logeado"
            return HttpResponseRedirect("ver_resenas") # Redireccionamos a ver_resenas
        else:   # Si no lo encuentra
            messages.error(request, "Usuario o contraseña incorrectos") # Mostramos mensaje de error
            return HttpResponseRedirect("login")    # Redireccionamos a login, nos quedamos donde mismo
    
# Definimos funcion para registrarse
def register(request):
    credenciales = Usuario.objects.all()

    if request.method == "GET": # Si se ingresa a la página antes de rellenar los datos
        # Render a la página con el formulario de register
        return render(request, "usuarios/register.html", {"credenciales": credenciales, "form_register": RegisterForm()})

    if request.method == "POST": # Si se ingresa luego de apretado el botón
        # Obtenemos las credenciales ingresadas
        username = request.POST["nombre"]
        password = request.POST["contraseña"]

        # Checkeo de que no exista el usuario
        if Usuario.objects.filter(username=username).exists():
            # Mostramos mensaje de error
            messages.error(request, "Nombre de usuario ya existente")
            return HttpResponseRedirect("register") # Nos quedamos donde mismo

        # Checkeo de largo
        if len(username) < 5:
            # Mostramos mensaje de error
            messages.error(request, "Nombre de usuario demasiado corto, debe ser a lo menos 5")
            return HttpResponseRedirect("register") # Nos quedamos donde mismo
        # Creamos el usuario en la BD
        usuario = Usuario.objects.create_user(username=username, password=password)
        return HttpResponseRedirect("login")    # Redireccionamos a register, nos quedamos donde mismo