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
