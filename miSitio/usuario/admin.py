from django.contrib import admin
from usuario.models import Cliente, Reserva, Habitacion


admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Habitacion)