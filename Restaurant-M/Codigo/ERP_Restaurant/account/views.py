from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, registrarGerente, registrarRestaurante
from .models import Gerentes, Restaurantes
from django.contrib import messages

# Este archivo se encarga de las vistas y la lógica de las mismas

# Incio funciones para tener al gerente actual
idGerente = '0'

def setGerenteAct(id):
    global idGerente
    idGerente = id

def getGerenteAct():
    return idGerente
# Final

# Esta es la vista del login y la de inicio, al ser llamada por el path sin url en "urls.py"
def vistaLogin(request):
    # Utilizamos el forulario de inicio (mas tarde te lo muestro)
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
                    setGerenteAct(gerente.idGerente)
                    return redirect('home')  # Nos redirige al Path con el nombre "home"
                else:
                    messages = 'Contraseña incorrecta'
            except Gerentes.DoesNotExist:
                messages= 'Correo no registrado'

    return render(request, 'ERP_Restaurant/login.html', {
        # Enviaremos datos al archivo html
        'form': form,
        'message': messages
    })

# Vista de los planes (No hace nada, ademas de mostrar los planes)
def vistaPlanes(response):
    return render(response, 'ERP_Restaurant/planes.html', {})

# Vista del registro del gerente
def vistaRegistroGer(request):
    # Utilizamos el formulario de gerentes (más tarde te lo muestro)
    form = registrarGerente()
    message = ''
    
    if request.method == "POST":
        form = registrarGerente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registroRes') # Nos redirige al Path con el nombre "registroRes"
        else:
            message = 'Revisa los errores en el formulario'
        
    return render(request, 'ERP_Restaurant/registroGer.html', {
        # Enviaremos datos al archivo html
        'formGer': form,
        'msg': message
    })

# Vista del registro del restaurante
def vistaRegistroRes(request):
    # Utilizamos el formulario de registro restaurantes
    form = registrarRestaurante()

    # Buscamos en el modelo "Gerentes" al ultimo en ser ingresado
    ger = Gerentes.objects.last()

    # Guadamos datos
    nomGer = ger.nombreGer if ger else "No asignado"
    idGer = ger.idGerente if ger else "No asignado"
    
    if request.method == "POST":
        form = registrarRestaurante(request.POST)
        if form.is_valid():
            form.save()
            setGerenteAct(idGer)
            return redirect('home') # Nos redirige al Path con el nombre "home"
    return render(request, 'ERP_Restaurant/registroRes.html', {
        # Enviaremos datos al archivo html
        'formRes': form,
        'idGer': idGer,
        'nomGer': nomGer,
    })

# Vista del home
def vistaHome(request):
    # Obtenemos el valor del gerente que inicio sesión
    idGer = getGerenteAct()
    
    ger = Gerentes.objects.filter(idGerente = idGer).first()
    
    nombreGer = ger.nombreGer if ger else "No asignado"
    
    res = Restaurantes.objects.filter(idGerente =  idGer).first()
    nomRes = res.nombreRes if res else "No asignado"

    return render(request, 'ERP_Restaurant/home.html', {
        # Enviaremos datos al archivo html
        'nombre_gerente': nombreGer,
        'nomRes': nomRes
    })

