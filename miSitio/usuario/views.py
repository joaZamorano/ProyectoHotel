from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'usuario/index.html', {})

def login(request):
    return render(request, 'usuario/login.html', {})

def administrador(request):
    if request.POST:
        reservas = Reservas()
        reservas.id = request.POST.get('id')
        reservas.diasReservados = request.POST.get('diasReservados')
        reservas.fechaReserva = request.POST.get('fechaReserva')
        reservas.rutCliente = request.POST.get('rutCliente')
        reservas.nHabitacion = request.POST.get('nHabitacion')
        

        try:
            reservas.save()
        except:
            mensaje = "No se ha podido agregar"
        return redirect('administrador')

    return render(request, 'usuario/administrador.html', {})   

def logout(request):
    return render(request, 'usuario/index.html', {})

def reservar(request):
    return render(request, 'usuario/reservar.html', {})

def registro(request):
    return render(request, 'usuario/registro.html', {})

def habitaciones(request):
    if request.POST:
        habitacion = Habitacion()
        habitacion.nHabitacion = request.POST.get('nHabitacion')
        habitacion.tipoHabitacion = request.POST.get('tipoHabitacion')
        habitacion.metroCuadrado = request.POST.get('metroCuadrado')
        habitacion.baños = request.POST.get('baños')
        habitacion.camas = request.POST.get('camas')   

        try:
            habitacion.save()
        except:
            mensaje = "No se ha podido agregar"
        return redirect('habitaciones')

 def Clientecrud(request):
    if request.POST:
        clientecrud = Clientecrud()
        clientecrud.rut = request.POST.get('rut')
        clientecrud.nombre = request.POST.get('nombre')
        clientecrud.apellido = request.POST.get('apellido')
        clientecrud.email = request.POST.get('email')
        clientecrud.fechaN = request.POST.get('fechaN')
        clientecrud.usuario = request.POST.get('usuario')
        clientecrud.contraseña = request.POST.get('contraseña')   

        try:
            clientecrud.save()
        except:
            mensaje = "No se ha podido agregar"
        return redirect('clientecrud')