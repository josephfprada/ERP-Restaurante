
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vistaModCliPro, name='homeCliPro'),
    path('clientes/nuevo/', views.vistaRegistroCli, name='agregarCli'),
    path('clientes/', views.vistaListarClientes, name="listarCli"),
]
