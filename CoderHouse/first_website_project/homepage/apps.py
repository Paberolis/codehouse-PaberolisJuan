from django.apps import AppConfig


class homepageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'homepage'

class Cursos(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cursos'

class Estudiantes(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alumnos'

class profesor(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profesores'