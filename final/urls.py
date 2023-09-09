from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', blog, name="blog"),
    path('contact/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros"),
]