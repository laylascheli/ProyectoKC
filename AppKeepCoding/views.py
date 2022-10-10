from django.http import HttpResponse
from django.shortcuts import render
from AppKeepCoding.models import Curso

def curso(self):
    curso = Curso(nombre = "Desarrollo Web", camada = 17645)
    curso.save()
    texto = f"Curso: {curso.nombre}, Camada: {curso.camada}"
    return HttpResponse(texto)