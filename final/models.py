from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatar")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()  # Cambia a TextField
    imagen = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    autor = models.CharField(max_length=70)

class Comentario(models.Model):
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    comentario = models.ForeignKey(Blog, related_name="comentario", on_delete=models.CASCADE, null=True
    )
    def __str__(self):
        return f"{self.nombre} - {self.comentario}"

