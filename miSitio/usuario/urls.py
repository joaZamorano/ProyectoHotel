from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
from .views import index, admin, habitaciones, login, logout, registro, reservar
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',index, name='index'),
    path('index/', index , name='index'),
    path('admin/', admin, name='admin'),
    path('login/',LoginView.as_view(template_name='usuario/login.html'), name="login"),
    path('index/',LogoutView.as_view(template_name='usuario/index.html'),name="logout"), 
    path('registro/', registro, name='registro'),
    path('registro/login', login, name='registro2'),
    path('reservar/',reservar, name='reservar'),
    path('habitaciones/', habitaciones, name='habitaciones')
]