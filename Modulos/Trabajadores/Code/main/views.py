from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import registrarEmpleado
from .models import Empleado

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def home(request):
    empleados = Empleado.objects.all()
    return render(request, "main/home.html", {"empleados": empleados})

def create(request):
    if request.method == "POST":
        form = registrarEmpleado(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = registrarEmpleado()
    
    return render(request, 'main/create.html', {'form': form})
