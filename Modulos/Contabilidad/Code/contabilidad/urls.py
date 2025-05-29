from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='Login'),
    path('index/', views.index, name='Index'),
    path('cuentas_contables/', views.gestion_cuentas_contables, name="CuentasContables"),
    path('tipos-cuenta/delete/<int:pk>/', views.delete_tipo_cuenta, name='BorrarTipoCuenta'),
    path('facturas/', views.gestion_facturas, name='GestionFacturas'),
    path('facturas/ver/<int:pk>/', views.ver_factura, name='VerFacturas'),
    path('facturas/editar/<int:pk>/', views.EditarFactura, name='EditarFactura'),
    path('facturas/eliminar/<int:pk>/', views.eliminar_factura, name='EliminarFacturas'),
    path('comprobantes/', views.gestion_comprobantes, name='GestionComprobantes'),
    path('comprobantes/subir/', views.subir_comprobante_general, name='SubirComprobanteGeneral'), 
    path('comprobantes/subir/<int:factura_pk>/', views.subir_comprobante_para_factura, name='SubirComprobanteParaFactura'),
    path('comprobantes/editar/<int:pk>/', views.editar_comprobante, name='EditarComprobante'),
    path('comprobantes/eliminar/<int:pk>/', views.eliminar_comprobante, name='EliminarComprobante'),
    path('reporte/contable/excel/', views.exportar_reporte_contable_excel, name='ExportarReporte'),
]