from django.db import models

<<<<<<< HEAD
# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    nacimiento = models.DateField(null = True)
    pais_origen_id =models.ForeignKey(Pais, on_delete=models.SET_NULL, null = True)
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
=======

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
>>>>>>> cb96a39ef72a5a2d840bafb3a7ef5818444326f4
