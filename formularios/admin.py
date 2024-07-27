from django.contrib import admin
from .models import *

class CursoAdmin(admin.ModelAdmin):
    list_display=("nombre","comision")
    list_per_page= 10
    list_filter=("nombre","comision" )
    ordering=("nombre",)

class ProfesorAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","email","especialidad")
    list_per_page= 10
    list_filter=("especialidad","apellido")
    ordering=("especialidad","apellido")

class EstudiandoAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","email")
    list_per_page= 10
    list_filter=("apellido",)
    ordering=("apellido",)

admin.site.register(Curso,CursoAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Estudiante,EstudiandoAdmin)
