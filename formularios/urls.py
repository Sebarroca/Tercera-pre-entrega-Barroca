from django.urls import path
from formularios.views import *
urlpatterns = [
    path('', inicio,name="inicio"),
    path('cursos/', cursos,name="curso"),
    path('estudiantes/', estudiantes,name="estudiantes"),
    path('profesores/', profesores,name="profesores"),
    path('buscarCurso/',buscarCurso,name="buscarCurso"),
    path('buscarProfesor/',buscarProfesor,name="buscarProfesor"),
    path('buscarEstudiante/',buscarEstudiante,name="buscarEstudiante"),
]
