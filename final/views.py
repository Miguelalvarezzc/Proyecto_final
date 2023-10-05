from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "final/home.html", {"avatar": obtenerAvatar(request)})

def blog(request):
    if request.method == 'POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            titu=info["titulo"]
            cont=info["contenido"]
            aut=info["autor"]
            form.save()
            return render(request, "final/blog.html", {"avatar": obtenerAvatar(request)})
        else:
            return render(request, "final/blog.html")
    else:
        form=BlogForm()
        return render(request,"final/blog.html", {"avatar": obtenerAvatar(request)})
    

def sobremi(request):
    return render(request,"final/sobremi.html", {"avatar": obtenerAvatar(request)})


def login_request(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None: 
                login(request, usuario)
                return render(request, "final/login.html", {"mensaje":f"Usuario {usu} logueado correctamente", "avatar": obtenerAvatar(request)})
            else:
                return render(request, "final/login.html", {"form":form, "mensaje":"Datos invalidos"})
        else:
            return render(request, "final/login.html", {"form":form, "mensaje":"Datos invalidos"})
    else:
        form=AuthenticationForm()
        return render(request, "final/login.html", {"form":form})

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render(request, "final/register.html", {"mensaje":f"Usuario {nombre_usuario} creado correctamente", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "final/register.html", {"form":form, "mensaje":"Datos invalidos"})
    else:
        form=UserRegisterForm()
        return render(request, "final/register.html", {"form":form})
    
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render (request, "final/inicio.html", {"mensaje":f" Usuario {usuario.username} editado correctamente", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "final/editarPerfil.html", {"form": form, "nombre usuario":usuario.userame, "mensaje":"Datos invalidos"})
    else:
        form=UserEditForm(instance=usuario)
        return render (request, "final/editarPerfil.html", {"form": form, "nombre usuario":usuario.username, "avatar": obtenerAvatar(request)})
    
def obtenerAvatar(request):
    avatar = Avatar.objects.filter(user=request.user.id)

    if len(avatar) != 0:
        return avatar[0].imagen.url
    else:
        return "/media/avatar/avatarpordefecto.jpg"
    
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])

            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render (request, "final/agregarAvatar.html", {"mensaje":"Avatar agregado correctamente", "avatar": obtenerAvatar(request)})
        else:
            return render (request, "final/agregarAvatar.html", {"form":form, "usuario":request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render (request, "final/agregarAvatar.html", {"form":form, "usuario":request.user, "avatar": obtenerAvatar(request)})
    
