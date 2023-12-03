from django.contrib import admin
from homepage import models
from .models import Curso, Estudiante, Profesor
# Register your models here.

admin.site.register(models.Curso)
admin.site.register(models.Profesor)
admin.site.register(models.Estudiante)
admin.site.register(models.Entregable)

