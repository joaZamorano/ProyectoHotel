from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from .views import index, admin, habitaciones, login, logout, registro, reservar
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',index, name='index'),
    path('index/', views.index , name='index'),
    path('admin/', views.admin, name='admin'),
    path('login/',LoginView.as_view(template_name='usuario/login.html'), name="login"),
    path('index/',LogoutView.as_view(template_name='usuario/index.html'),name="logout"), 
    path('registro/', views.registro, name='registro'),
    path('registro/login', views.login, name='registro2'),
    path('reservar/',views.reservar, name='reservar'),
    path('habitaciones/', views.habitaciones, name='habitaciones'),
    path('index/login',views.login, name='login'),
    path('reservar/index',views.reservar, name='reservar')
    
]