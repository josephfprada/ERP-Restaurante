from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="Login"),
    path("main/", views.home, name="Home"),
    path("main/create/", views.registrar_empleado, name="CrearEmpleado"),
    path('registrar-empleado/', views.registrar_empleado, name='registrar_empleado'),
    path('subir-documento/', views.subir_documento_empleado, name='subir_documento_empleado'),
    path('subir-documento/<int:empleado_id>/', views.subir_documento_empleado_con_id, name='subir_documento_empleado_con_id'),
    path('empleado/<int:empleado_id>/subir-hoja-vida/', views.subir_hoja_vida_empleado, name='subir_hoja_vida_empleado'),
    path('documento/subir/', views.subir_documento_empleado, name='subir_documento_empleado'),
    path('empleados/perfiles/', views.perfiles_empleados, name='perfil_empleado_lista'),
    path('empleados/<int:empleado_id>/editar/', views.empleado_detalle_editar, name='empleado_detalle_editar'),
    path('empleados/<int:empleado_id>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'),
    path('exportar_empleados_excel/', views.exportar_empleados_excel, name='exportar_empleados_excel'),
    path('empleado/<int:empleado_id>/evaluar/', views.realizar_evaluacion, name='realizar_evaluacion'),
    path('empleado/<int:empleado_id>/guardar_evaluacion/', views.guardar_evaluacion, name='guardar_evaluacion'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)