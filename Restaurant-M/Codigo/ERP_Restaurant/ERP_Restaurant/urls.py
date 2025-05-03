
from django.contrib import admin
from django.urls import path, include

# Aquí encontraremos los links o paths que nos redirigen en la aplicación
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')), # Al no tener ningun url al principo, se tratara como el path de inicio
    path('RRHH/', include('Recursos_Humanos.urls')),
    path('Cli_Pro/', include('clientes_Proveedores.urls')),
    # Estas path son por cada app (en este archivo), al crear una nueva app
    # tendras qu escribirlo con la estructura
]