from django.contrib import admin
from .models import (
    Empleado, Departamento, EmpleadoDepartamento, 
    Capacitacion, Beneficios, Desempeno, Permiso, RelacionLaboral
)

#Implementacion de las extenciones necesarias - BD
admin.site.register(Empleado)
admin.site.register(Departamento)
admin.site.register(EmpleadoDepartamento)
admin.site.register(Capacitacion)
admin.site.register(Beneficios)
admin.site.register(Desempeno)
admin.site.register(Permiso)
admin.site.register(RelacionLaboral)
