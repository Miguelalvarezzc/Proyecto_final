from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from final.models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E_mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Modificar Nombre")
    last_name=forms.CharField(label="Modificar Apellido")
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k: "" for k in fields}

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")

class BlogForm(forms.Form):
    titulo=forms.CharField(max_length=200)
    contenido = forms.CharField()
    imagen = forms.ImageField(upload_to='blog_images/', blank=True, null=True)
    autor = forms.CharField(max_length=70)
    class Meta:
        model = Blog
        fields = ['titulo', 'contenido', 'imagen', 'autor']
