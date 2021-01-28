from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
from .views import index, admin, habitaciones, login, logout, registro, reservar
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',index, name='index'),
    path('index.html/', index , name='index'),
    path('admin.html/', admin, name='admin'),
    path('login.html/',LoginView.as_view(template_name='usuario/login.html'), name="login"),
    path('logout.html/',LogoutView.as_view(template_name='usuario/index.html'),name="logout"), 
    path('registro.html/', registro, name='registro'),
    path('reservar.html/',reservar, name='reservar'),
    path('habitaciones.html/', habitaciones, name='habitaciones')
]