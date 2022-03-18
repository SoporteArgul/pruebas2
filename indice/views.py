
from django.http import HttpResponse
import random
from django.template import Context,Template,loader 

def inicio(request):
    return HttpResponse('Hola mundo')

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
    
    """version moderna"""
    template=loader.get_template("mi_plantilla.html")  
    plantilla_preparada= template.render(diccionario)
    return HttpResponse(plantilla_preparada)

