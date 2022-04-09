from django.db import models
from stat import FILE_ATTRIBUTE_DIRECTORY
from django.forms import CharField

# Create your models here.
class Familiar (models.Model):
    nombre = models.CharField("Nombre",max_length=30, default = "ingrese nombre")
    apellido = models.CharField("Apellido",max_length=30, default = "ingrese apellido")
    edad = models.IntegerField("Edad")
    fecha_nac = models.DateField("Fecha de Nacimiento")
    relacion = models.CharField("Parentesco",max_length=30,default = "ingrese parentesco")

    def __str__(self) -> str:
        return f"{self.nombre}-{self.apellido}-{self.edad}-{self.fecha_nac}-{self.relacion}" 