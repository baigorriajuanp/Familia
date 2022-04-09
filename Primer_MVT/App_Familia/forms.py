from django import forms

class FamiliaForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_de_nacimiento = forms.DateField()    
    relacion = forms.CharField(max_length=30)
