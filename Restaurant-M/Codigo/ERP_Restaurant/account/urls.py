
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vistaLogin, name='login'),
    path('planes/', views.vistaPlanes, name='planes'),
    path('registro/', views.vistaRegistro, name='registro'),
    #path('home/', views.vistaHome, name='home'),
]
