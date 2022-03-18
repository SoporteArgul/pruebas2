from .views import inicio,otra_vista,numero_random,mi_plantilla
from django.urls import path

urlpatterns=[  
    path('inicio/',inicio),
    path('otra_vista/',otra_vista),
    path('rand/',mi_plantilla),]