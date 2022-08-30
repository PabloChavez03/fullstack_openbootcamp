from pyexpat import model
from django.db import models

# Create your models here.

class Director(models.Model):
    nombre = models.CharField(max_length=32, help_text="Pon nombre del director")
    apellido = models.CharField(max_length=32, help_text="Pon apellido del director")
    brithday = models.DateField(help_text="Fecha de nacimiento")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pelicula(models.Model):
    titulo = models.CharField(max_length=32, help_text="Pon el nombre de la pelicula")
    fecha_de_estreno = models.DateTimeField(help_text="Fecha de estreno")
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=400, help_text="Pon un resumen")

    def __str__(self):
        return self.titulo



