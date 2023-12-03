from django.shortcuts import render, redirect
from homepage.forms import CursoFormulario, ProfesorFormulario, EstudiantesFormulario
from .models import Curso, Profesor, Estudiante
import logging
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'homepage/home.html')

def Cursos(request):
    return render(request, 'homepage/cursos.html')

def Estudiantes(request):
    return render(request, 'homepage/estudiantes.html')

def Profesores(request):
    return render(request, 'homepage/profesores.html')

 # Asegúrate de importar tu modelo Curso

def cursoformulario(request):
    if request.method == "POST":
        form = CursoFormulario(request.POST)  # Aquí me llega la información del HTML
        if  form.is_valid():  # Corregir la llamada a is_valid
            informacion = form.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "homepage/home.html")
    else:
        form = CursoFormulario()
    return render(request, 'homepage/curso_formulario.html', {"miFormulario": form})

  
def profesorformulario(request):
      if request.method == "POST":
            form1 = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
            if form1.is_valid():
                  informacion = form1.cleaned_data
                  profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], materia=informacion["materia"])
                  profesor.save()
                  return render(request, "homepage/home.html") # vuela al inicio o a donde quieran
      else:
            form1 = ProfesorFormulario() # Formulario vacio para construir el html
      return render(request, "homepage/profesores_formulario.html", {"miFormulario": form1})


def estudianteformulario(request):
      if request.method == "POST":
            form = EstudiantesFormulario(request.POST) # Aqui me llega la informacion del html
            if form.is_valid():
                  informacion = form.cleaned_data
                  estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
                  estudiante.save()
                  return render(request, "homepage/home.html") # vuela al inicio o a donde quieran
      else:
            form= EstudiantesFormulario() # Formulario vacio para construir el html
      return render(request, "homepage/estudiantes_formulario.html", {"miFormulario": form})

def busquedaCamada(request):
    return render(request, 'homepage/busqueda_camada.html')

def buscar(request):
    if request.GET['camada']:
        # respuesta = f'Estoy buscando la camada nro: {request.GET["camada"]}'
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, 'homepage/resultadosBusqueda.html', {'cursos': cursos, 'camada': camada})
    else:
        respuesta = 'No enviaste datos.'

    # No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)


def busquedaProfesor(request):
    return render(request, 'homepage/busqueda_profesor.html')

def buscarP(request):
    if request.GET['materia']:
        # respuesta = f'Estoy buscando el profesor de la materia: {request.GET["materia"]}'
        materia = request.GET['materia']
        profesor = Profesor.objects.filter(materia__icontains=materia)

        return render(request, 'homepage/resultadosBusquedaP.html', {'profesor': profesor,'materia': materia  })
    else:
        respuesta = 'No enviaste datos.'

    # No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)

def busquedaAlumno(request):
    return render(request, 'homepage/busqueda_alumno.html')

def buscarA(request):
    if request.GET['apellido']:
        # respuesta = f'Estoy buscando el profesor de la materia: {request.GET["materia"]}'
        apellido = request.GET['apellido']
        estudiante = Estudiante.objects.filter(apellido__icontains=apellido)
        return render(request, 'homepage/resultadosBusquedaA.html', {'apellido': apellido,'estudiante': estudiante  })
    else:
        respuesta = 'No enviaste datos.'

    # No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)