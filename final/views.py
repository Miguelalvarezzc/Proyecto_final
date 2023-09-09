from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"final/home.html")

def blog(request):
    return render(request,"final/blog.html")

def contacto(request):
    return render(request,"final/contacto.html")

def nosotros(request):
    return render(request,"final/nosotros.html")

def registrar(request):
    return render(request,"final/registrar.html")