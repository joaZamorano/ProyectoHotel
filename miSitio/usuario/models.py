from django.db import models
from django.contrib import admin
from miSitio.usuario.models import Author

admin.site.register(Author)

class Cliente(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    fechaN = models.DateField(blank=False, null=False)
    usuario = models.CharField(max_length=12,blank=False)
    contraseña = models.CharField(max_length=8, blank=False)

class Habitacion(models.Model):
    nHabitacion = models.IntegerField(primary_key=True)
    tipoHabitacion = models.CharField(max_length=20)
    metroCuadrado = models.IntegerField()
    baños = models.IntegerField()
    camas = models.IntegerField()

class Reserva(models.Model):
    id = models.IntegerField(primary_key=True)
    diasReservados = models.IntegerField(blank=False)
    fechaReserva = models.DateField()
    rutCliente = models.ForeignKey(Cliente,null=False, blank=False, on_delete=models.CASCADE)
    nHabitacion = models.ForeignKey(Habitacion, null=False,blank=False,on_delete=models.CASCADE)