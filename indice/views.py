
from django.http import HttpResponse
import random
#from django.template import Context,Template,loader 
from django.shortcuts import redirect, render
from django.contrib.auth import login ,authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request,'indice/index.html',{})

def otra_vista(request):
    return HttpResponse('''
         <h1>HOLAAAAAAAAAAAAAA</h1> 
    
    ''')

def numero_random(request):
    numero=random.randint(1,10100000)
    return HttpResponse(numero)

def mi_plantilla(request):
    """version vieja"""
    #plantilla=open(r"C:\Users\user\Desktop\Proyecto2\miproyecto\plantillas\mi_plantilla.html")
    #template=Template(plantilla.read())
    #contexto=Context(diccionario)
    
    nombre='mateo'
    apellido='lonzayes'
    diccionario = {
        'nombre':nombre,
        'apellido':apellido,
        'largo':len(nombre)
    }
    
    """version moderna sin optimizar"""
    #template=loader.get_template("mi_plantilla.html")  
    #plantilla_preparada= template.render(diccionario)
    #return HttpResponse(plantilla_preparada)
    """verison moderna optimizada"""
    return render(request,"indice/mi_plantilla.html",diccionario) 

def login_request(request):
    #django_login,authenticate
    
    if request.method =='POST':
       form=AuthenticationForm(request, data=request.POST)
       if form.is_valid():
           username=form.cleaned_data['username']
           password=form.cleaned_data['password']
           user=authenticate(username=username,password=password)
           if user is not None:
               login(request,user)
               return render(request,'indice/index.html',{'msg':'Te logueaste!'})
           else:
               return render(request,'indice/login.html',{'form':form, 'msg': 'Error vuelva a intentarlo'})
       else:
          return render(request,'indice/login.html',{'form':form,'msg':'info erronea'})
    else:
        form=AuthenticationForm()   
        return render(request,'indice/login.html',{'form':form,'msg':''})


def register(request):    
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,'indice/index.html',{'mensage':f'usuario creado {username}:)'})
        else:
            return render(request,'indice/register.html',{'form':form, 'msg':''})
    else:
        form=UserRegisterForm()
    return render(request,'indice/register.html',{'form':form})
    
    
@login_required
def edit_profile(request):
    usuario=request.user
    if request.method == 'POST':
        miFormulario=UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']        
            usuario.password2=informacion['password2']
            usuario.save()
            return render(request,'indice/index.html',{})
    else:
        miFormulario=UserEditForm(initial={'email':usuario.email})
    return render(request,'indice/editprofile.html',{'miFormulario':miFormulario,'usuario':usuario})