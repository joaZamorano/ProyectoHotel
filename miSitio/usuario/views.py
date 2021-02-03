from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'usuario/index.html', {})

def login(request):
    return render(request, 'usuario/login.html', {})

def admin(request):
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
    return render(request, 'usuario/Habitaciones reservadas.html', {})

 