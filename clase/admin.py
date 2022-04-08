from django.contrib import admin
from .models import curso,profesor,Entregable, Estudiante
# Register your models here.

admin.site.register(curso)
admin.site.register(profesor)
admin.site.register(Entregable)
admin.site.register(Estudiante)