
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vistaLogin, name='login'),
    path('planes/', views.vistaPlanes, name='planes'),
    path('registroGer/', views.vistaRegistroGer, name='registroGer'),
    path('registroRes/', views.vistaRegistroRes, name='registroRes'),
    path('home/', views.vistaHome, name='home'),
]
