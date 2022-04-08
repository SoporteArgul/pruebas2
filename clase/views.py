from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render,redirect
from clase.models import Estudiante, curso,profesor
from clase.forms import BusquedaCurso, CursoFormulario,EstudianteFormulario
import random
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def nuevo_curso(request):
    camada=random.randrange(1000,9999)
    nuevo_curso= curso(nombre='Curso JS', camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"se creo el curso{nuevo_curso.nombre} camada {nuevo_curso.camada}")

@login_required
def formulario_curso(request):
    #sin formulario django
    #if request.method =='POST':
     #   nuevo_curso= curso(nombre=request.POST['curso'], camada=request.POST['camada'])
      #  nuevo_curso.save()
       # print(request.POST)
        #return render(request,'indice/index.html',{'nuevo_curso': nuevo_curso})
    #return render(request,'indice/formulario_curso.html',{})
    if request.method =='POST':
        formulario=CursoFormulario(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            nuevo_curso= curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()
        return render(request,'indice/index.html',{'nuevo_curso': nuevo_curso})
            

    formulario=CursoFormulario()
    return render(request,'clase/formulario_curso.html',{'formulario':formulario})

@login_required
def busqueda_curso(request):
    curso_buscado=[]
    dato=request.GET.get('partial_curso',None)
    if dato is not None:
       #curso_buscado=curso.objects.filter(curso=dato)
       curso_buscado=curso.objects.filter(nombre__icontains=dato)
    buscador=BusquedaCurso()   
    return render(request,'clase/busqueda_curso.html',{'buscador' : buscador, 
                                                       'cursos_buscados':curso_buscado,
                                                       'dato':dato})


# CRUD BASICO
@login_required
def crear_estudiante(request):
    if request.method =='POST':
        formulario=EstudianteFormulario(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            nuevo_estudiante= Estudiante(
                nombre=data['nombre'], 
                apellido=data['apellido' ],
                email=data['email'])
            nuevo_estudiante.save()
        #return render(request,'clase/listado_estudiante.html',{})
        return redirect('listado_estudiante')
    formulario=EstudianteFormulario()
    return render(request,'clase/crear_estudiante.html',{ 'formulario': formulario })

@login_required
def listado_estudiante(request):
    listado_estudiante=Estudiante.objects.all()
    return render(request,'clase/listado_estudiante.html',{'listado_estudiante':listado_estudiante})


def actualizar_estudiante(request,id):
     
     estudiante=Estudiante.objects.get(id=id)
     
     if request.method =='POST':
     
        formulario=EstudianteFormulario(request.POST)
     
        if formulario.is_valid():
     
          data=formulario.cleaned_data
     
          estudiante.nombre=data['nombre']
     
          estudiante.apellido=data['apellido']
     
          estudiante.email=data['email']
     
          estudiante.save()
        return redirect('listado_estudiante')
     
     formulario=EstudianteFormulario(
         initial=
         {
         'nombre':estudiante.nombre,
         'apellido':estudiante.apellido,
         'email':estudiante.email
         }
     )
     return render(request,'clase/actualizar_estudiante.html',
                 { 'formulario': formulario, 
                   'estudiante': estudiante
                 })
    

def borrar_estudiante(request,id):
    estudiante=Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect('listado_estudiante')
    
#CRUD CON CLASES BASADAS EN VISTAS
#class profesor(models.Model):
""" nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)"""

class ProfesorLista(LoginRequiredMixin,ListView):
    model=profesor
    template_name='/clase/profesor_list.html'


class ProfesorDetalle(DetailView,LoginRequiredMixin):
    model=profesor
    template_name='clase/profesor_datos.html'


class ProfesorEditar(UpdateView,LoginRequiredMixin):
    model=profesor
    success_url='/clase/profesores'  #nos movemos entre path no entre names
    fields=['nombre','apellido','email','profesion']


class ProfesorBorrar(DeleteView,LoginRequiredMixin):
    model=profesor
    success_url='/clase/profesores'
    
class ProfesorCrear(CreateView,LoginRequiredMixin):
    model=profesor
    success_url='/clase/profesores'  
    fields=['nombre','apellido','email','profesion']


