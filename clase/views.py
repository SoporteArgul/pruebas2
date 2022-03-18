from django.http import HttpResponse
from django.shortcuts import render
from clase.models import curso
import random
# Create your views here.


def nuevo_curso(request):
    camada=random.randrange(1000,9999)
    nuevo_curso= curso(nombre='Curso JS', camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"se creo el curso{nuevo_curso.nombre} camada {nuevo_curso.camada}")

