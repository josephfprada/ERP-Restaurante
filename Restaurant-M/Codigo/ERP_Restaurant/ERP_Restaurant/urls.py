
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('RRHH/', include('Recursos_Humanos.urls')),
    path('Cli_Pro/', include('clientes_Proveedores.urls')),
]
