from django.contrib import admin
from .models import Cliente,  Habitacion, Reserva

admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Habitacion)