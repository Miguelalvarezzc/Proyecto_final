from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('blog/', blog, name="blog"),
    path('sobremi/', sobremi, name="sobremi"),
    path('login/', login_request, name="login"),
    path('register', register, name='register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarPerfil', editarPerfil, name="editarPerfil" ),
    path('agregarAvatar', agregarAvatar, name="agregarAvatar"),
]