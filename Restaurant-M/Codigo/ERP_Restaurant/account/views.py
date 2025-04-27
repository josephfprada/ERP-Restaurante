from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, registrarGerente, registrarRestaurante
from .models import Gerentes, Restaurantes
from django.contrib import messages

def vistaLogin(request):
    form = LoginForm()
    messages = ''

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                gerente = Gerentes.objects.get(emailGer=email)
                if gerente.passwordGer == password:
                    request.session['gerente_id'] = gerente.idGerente
                    request.session['gerente_nombre'] = gerente.nombreGer
                    return redirect('home')  # Reemplaza con tu vista principal
                else:
                    messages = 'Contraseña incorrecta'
            except Gerentes.DoesNotExist:
                messages= 'Correo no registrado'

    return render(request, 'ERP_Restaurant/login.html', {
        'form': form,
        'message': messages
    })

# Vista de los planes
def vistaPlanes(response):
    return render(response, 'ERP_Restaurant/planes.html', {})

# Vista del registro del gerente
def vistaRegistroGer(request):
    form = registrarGerente()
    message = ''
    
    if request.method == "POST":
        form = registrarGerente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registroRes')
        else:
            message = 'Revisa los errores en el formulario'
        
    return render(request, 'ERP_Restaurant/registroGer.html', {
        'formGer': form,
        'msg': message
    })

# Vista del registro del restaurante
def vistaRegistroRes(request):
    form = registrarRestaurante()

    ger = Gerentes.objects.last()

    nomGer = ger.nombreGer if ger else "No asignado"
    idGer = ger.idGerente if ger else "No asignado"
    
    if request.method == "POST":
        form = registrarRestaurante(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'ERP_Restaurant/registroRes.html', {
        'formRes': form,
        'idGer': idGer,
        'nomGer': nomGer,
    })

# Vista del home
def vistaHome(request):
    ger = Gerentes.objects.last()

    nombreGer = ger.nombreGer if ger else "No asignado"

    return render(request, 'ERP_Restaurant/home.html', {
        'nombre_gerente': nombreGer
    })

