from django import forms

class CursoForm(forms.Form):
    nombre=forms.CharField(max_length=30) 
    comision=forms.IntegerField()     

class EstudianteForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    curso=forms.CharField(max_length=30)    
    email=forms.EmailField()                  

class ProfesorForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()
    especialidad=forms.CharField(max_length=30)