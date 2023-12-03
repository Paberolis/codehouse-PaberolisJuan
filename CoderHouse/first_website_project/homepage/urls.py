from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('cursos', views.Cursos, name="Cursos"),
    path('cursosFormulario', views.cursoformulario, name="CursosFormulario"),
    path('profesores', views.Profesores, name="Profesores"),
    path('profesorFormulario', views.profesorformulario, name="ProfesorFormulario"),
    path('estudiantes', views.Estudiantes, name="Estudiantes"),
    path('estudiantesFormularios', views.estudianteformulario, name="EstudiantesFormulario"),
    path('busquedaCamada', views.busquedaCamada, name="busquedaCamada"),
    path('buscar', views.buscar, name="buscar"),
    path('busquedaProfesor', views.busquedaProfesor, name="busquedaProfesor"),
    path('buscarP', views.buscarP, name="buscarP"),
    path('busquedaAlumno', views.busquedaAlumno, name="busquedaAlumno"),
    path('buscarA', views.buscarA, name="buscarA"),
    path('home', views.Home),
    
]