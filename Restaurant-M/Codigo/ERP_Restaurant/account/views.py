from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Vista del login
def vistaLogin(request):
    form = LoginForm(request.POST or None)
    message = ''
    
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                
                if user is not None:
                    login(request, user)
                    return redirect('home')  # Cambia esto a la URL que quieras redirigir
                else:
                    message = 'Credenciales inválidas'
            except User.DoesNotExist:
                message = 'El usuario no existe'

    return render(request, 'ERP_Restaurant/login.html', {'form': form, 'message': message})

# Vista de los planes
def vistaPlanes(response):
    return render(response, 'ERP_Restaurant/planes.html', {})

# Vista del registro
def vistaRegistro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'ERP_Restaurant/registro.html',{
                  'form': form,
                  'tittle': 'Registro'})