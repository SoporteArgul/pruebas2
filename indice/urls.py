from cgitb import html
from unicodedata import name
from .views import register,inicio, login_request,otra_vista,mi_plantilla,edit_profile
from django.urls import path
from django.contrib.auth.views import LogoutView
urlpatterns=[  
    path('',inicio, name='inicio'),
    path('otra_vista/',otra_vista, name='otra_vista'),
    path('mi_plantilla/',mi_plantilla,name='mi_plantilla'),
    path('login/',login_request ,name='login'),
    path('register/',register, name='register'),
    path('logout/',LogoutView.as_view(template_name='indice/logout.html'),name='logout'),
    path('editprofile/,',edit_profile,name='editprofile')]