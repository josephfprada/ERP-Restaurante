from datetime import date
import openpyxl
from .forms import RegistrarEmpleadoForm, DocumentoForm, EvaluacionDesempenoForm
from .models import Documentos, Empleado
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import csv

# Create your views here.

def index(request):
    return render(request, "main/login.html", {})

def home(request):
    empleados = Empleado.objects.all()
    return render(request, "main/inicio.html", {"empleados": empleados})

def registrar_empleado(request):
    if request.method == 'POST':
        form = RegistrarEmpleadoForm(request.POST)
        if form.is_valid():
            try:
                empleado = form.save()
                messages.success(request, f'Empleado {empleado.nombreEmpleado} {empleado.apellidoEmpleado} registrado exitosamente. Ahora, sube su hoja de vida.')
                return redirect('subir_documento_empleado_con_id', empleado_id=empleado.idEmpleado)
            except Exception as e:
                messages.error(request, f'Error al registrar empleado: {e}')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario de empleado.')
    else:
        form = RegistrarEmpleadoForm()
    return render(request, 'main/registrar_empleado.html', {'form': form})

def subir_documento_empleado(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, '¡Documento subido exitosamente!')
                return redirect('subir_documento_empleado')
            except Exception as e:
                messages.error(request, f'Hubo un error al subir el documento: {e}')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = DocumentoForm()
    empleados = Empleado.objects.all()
    return render(request, 'main/subir_documento.html', {'form': form, 'empleados': empleados})

def subir_documento_empleado_con_id(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)

    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            documento_obj = form.save(commit=False)
            documento_obj.idEmpleado = empleado
            documento_obj.save()
            messages.success(request, f'Hoja de vida para {empleado.nombreEmpleado} subida exitosamente.')
            return render(request, 'main/inicio.html')
        else:
            messages.error(request, 'Por favor, corrige los errores al subir la hoja de vida.')
    else:
        form = DocumentoForm(initial={'idEmpleado': empleado.idEmpleado, 'tipo_documento': 'Hoja de Vida', 'fecha_actualizacion': date.today()})

    empleados = Empleado.objects.all()
    return render(request, 'main/inicio.html', {'form': form, 'empleados': empleados, 'empleado_actual': empleado})

def perfiles_empleados(request):
    empleados = Empleado.objects.all().order_by('apellidoEmpleado', 'nombreEmpleado') 
    return render(request, "main/perfiles_empleados.html", {"empleados": empleados})

def empleado_detalle(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    return render(request, "main/empleado_detalles.html", {"empleado": empleado})

def empleado_detalle_editar(request, empleado_id):
    empleado = get_object_or_404(Empleado, idEmpleado=empleado_id)
    if request.method == 'POST' and 'save' in request.POST:
        form = DocumentoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, f'El perfil de {empleado.nombreEmpleado} {empleado.apellidoEmpleado} ha sido actualizado.')
            return redirect('empleado_detalle_editar', empleado_id=empleado.idEmpleado)
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = DocumentoForm(instance=empleado)
    return render(request, 'main/empleado_detalle_editar.html', {'form': form, 'empleado': empleado})

def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, idEmpleado=empleado_id)
    if request.method == 'POST':
        Documentos.objects.filter(idEmpleado=empleado).delete()
        empleado.delete()
        messages.success(request, f'El empleado {empleado.nombreEmpleado} {empleado.apellidoEmpleado} y sus documentos han sido eliminados.')
        return redirect('perfil_empleado_lista')
    else:
        return redirect('Home')

def subir_hoja_vida_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, idEmpleado=id_empleado)
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            hoja_vida = form.save(commit=False)
            hoja_vida.empleado = empleado
            hoja_vida.save()
            return redirect('perfil_empleado_lista')
    else:
        form = DocumentoForm()
    return render(request, 'subir_hoja_vida.html', {'form': form, 'empleado': empleado})

def realizar_evaluacion(request, empleado_id):
    empleado = get_object_or_404(Empleado, idEmpleado=empleado_id)
    form = EvaluacionDesempenoForm()
    context = {
        'empleado': empleado,
        'form': form,
    }
    return render(request, 'main/realizar_evaluacion.html', context)

def guardar_evaluacion(request, empleado_id):
    empleado = get_object_or_404(Empleado, idEmpleado=empleado_id)
    if request.method == 'POST':
        form = EvaluacionDesempenoForm(request.POST)
        if form.is_valid():
            evaluacion = form.save(commit=False)
            evaluacion.empleado = empleado
            evaluacion.save()
            messages.success(request, f'Evaluación de desempeño para {empleado.nombreEmpleado} {empleado.apellidoEmpleado} guardada correctamente.')
            return redirect('perfil_empleado_lista')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario de evaluación.')
            context = {
                'empleado': empleado,
                'form': form,
            }
            return render(request, 'main/realizar_evaluacion.html', context)
    else:
        return redirect('realizar_evaluacion', empleado_id=empleado_id)
    
def exportar_empleados_excel(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="empleados.xlsx"'

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = 'Empleados'

    # Encabezados
    header = ['ID', 'Nombre', 'Apellido', 'Puesto', 'Estado']
    worksheet.append(header)

    # Datos de los empleados
    empleados = Empleado.objects.all()
    for empleado in empleados:
        row = [empleado.idEmpleado, empleado.nombreEmpleado, empleado.apellidoEmpleado, empleado.puesto, empleado.estado]
        worksheet.append(row)

    workbook.save(response)
    return response