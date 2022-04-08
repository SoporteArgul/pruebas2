from django.db import models


class Estudiante(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Entregable(models.Model):
    nombre=models.CharField(max_length=20)
    fechaDeEntrega=models.DateField()
    Entregado=models.BooleanField()



class curso(models.Model):
    nombre=models.CharField(max_length=20)
    camada=models.IntegerField()
    def __str__(self):
        return f'{self.nombre} {self.camada}'


class profesor(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'