from django.urls import path
from .views import nuevo_curso
urlpatterns = [
    path('clase/',nuevo_curso ,name='nuevo_curso')    
]
