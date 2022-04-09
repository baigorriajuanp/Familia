from django.shortcuts import render
from django.forms import CharField
from django.http import HttpResponse
from .forms import FamiliaForm
from .models import Familiar
from django.template.context import Context
# Create your views here.


def inicio(request):
    return render(request,"index_familia.html")
    

def carga_familiar(request):
    if request.method == "POST":
        myform = FamiliaForm(request.POST)
        if myform.is_valid:
            print(myform)
            datos = myform.cleaned_data        
            familiar = Familiar (nombre = datos["nombre"], apellido = datos["apellido"], edad = datos["edad"], fecha_nac = datos["fecha_de_nacimiento"], relacion = datos["relacion"] )
            familiar.save()
            return render(request, "familiar_cargado.html")
    else:
        myform = FamiliaForm()
    return render (request,"carga_familiar.html",{"myform":myform})

def mostrar_familia(request):

    mi_familia = Familiar.objects.all()
    print(type({'familia':mi_familia}))
    return render(request,"ver_familiares.html",{'familia':mi_familia})