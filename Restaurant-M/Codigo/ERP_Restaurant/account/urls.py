
from django.urls import path
from . import views

# Vemos una mayor cantidad de paths, puesto que aquí cada path es una pagina html
urlpatterns = [
    path('', views.vistaLogin, name='login'),   # Url vacía significa que aquí comienza la aplicación
    path('planes/', views.vistaPlanes, name='planes'),
    path('registroGer/', views.vistaRegistroGer, name='registroGer'),
    path('registroRes/', views.vistaRegistroRes, name='registroRes'),
    path('home/', views.vistaHome, name='home'),
]

# Es immportante saber que todas las Path son importar si estan en app diferentes,
# deben tener un nombre único
# Ya que los path pueden ser llamados incluso si la llamada es desde otra app