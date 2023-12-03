from django import forms
from .models import Curso, Estudiante, Profesor

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido =  forms.CharField(max_length=30)
    email =  forms.CharField()
    materia =  forms.CharField(max_length=30)

class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido =  forms.CharField(max_length=30)
    email =  forms.CharField()
    