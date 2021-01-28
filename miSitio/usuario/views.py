from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'usuario/index.html', {})

def login(request):
    return render(request, 'usuario/login.html', {})

def admin(request):
    return render(request, 'usuario/admin.html', {})

def logout(request):
    return render(request, 'usuario/index.html', {})

def reservar(request):
    return render(request, 'usuario/reservar.html', {})

def registro(request):
    return render(request, 'usuario/registro.html', {})

def habitaciones(request):
    return render(request, 'usuario/Habitaciones reservadas.html', {})
    