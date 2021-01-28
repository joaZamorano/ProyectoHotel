from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    fechaN = models.DateField(blank=False, null=False)
    usuario = models.CharField(blank=False)
    contraseña = models.CharField(blank=False)

class Habitacion(models.Model):
    nHabitacion = models.IntegerField(primary_key=True)
    tipoHabitacion = models.CharField()
    metroCuadrado = models.IntegerField()
    baños = models.IntegerField()
    camas = models.IntegerField()

class Reserva(models.Model):
    id = models.IntegerField(primary_key=True)
    diasReservados = models.IntegerField(blank=False)
    fechaReserva = models.DateField()
    rutCliente = models.ForeignKey(Cliente,null=False, blank=False, on_delete=models.CASCADE)
    nHabitacion = models.ForeignKey(Habitacion, null=False,blank=False,on_delete=models.CASCADE)