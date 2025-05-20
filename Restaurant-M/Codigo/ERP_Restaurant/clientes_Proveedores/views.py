from django.shortcuts import render
from account.views import getGerenteAct
from account.models import Gerentes, Restaurantes
from .models import Clientes
from .form import registrarCliente, opBuscarCliente

idGerente = 0

def setGerAct(id):
    global idGerente
    idGerente = id

def getGerAct():
    return idGerente

# Vista de la pagina principal del modulo de clientes y proveedores
def vistaModCliPro(request):
    setGerAct(getGerenteAct())
    
    idGer = getGerAct()
    
    ger = Gerentes.objects.filter(idGerente = idGer).first()
    nombreGer = ger.nombreGer if ger else "No asignado"
    
    res = Restaurantes.objects.filter(idGerente =  idGer).first()
    nomRes = res.nombreRes if res else "No asignado"

    return render(request, 'html/homeCli.html', {
        'nombre_gerente': nombreGer,
        'nomRes': nomRes
    })
    
# Vista del registro del cliente
def vistaRegistroCli(request):
    form = registrarCliente()
    message = ''
    
    idGer = getGerAct()
    
    ger = Gerentes.objects.filter(idGerente = idGer).first()
    nombreGer = ger.nombreGer if ger else "No asignado"
    
    res = Restaurantes.objects.filter(idGerente =  idGer).first()
    nomRes = res.nombreRes if res else "No asignado"
    idRestaurante = res.idRestaurante if res else "No asignado"
    
    if request.method == "POST":
        form = registrarCliente(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'html/homeCli.html')
        else:
            message = 'Revisa los errores en los datos'
        
    return render(request, 'html/agregarCli.html', {
        'formCli': form,
        'msg': message,
        'nombre_gerente': nombreGer,
        'nomRes': nomRes,
        'idRes': idRestaurante,
    })
    
# Vista para ver los clientes
def vistaListarClientes(request):
    idGer = getGerAct()
    
    ger = Gerentes.objects.filter(idGerente = idGer).first()
    nombreGer = ger.nombreGer if ger else "No asignado"
    
    res = Restaurantes.objects.filter(idGerente =  idGer).first()
    nomRes = res.nombreRes if res else "No asignado"
    idRes = res.idRestaurante if res else "0"

    clientes = Clientes.objects.filter(idRestaurante = idRes)
    return render(request, 'html/listarCli.html', {
        'clientes': clientes,
        'nombre_gerente': nombreGer,
        'nomRes': nomRes,
    })
    
# Vista para ver los clientes
def vistaActualizarClientes(request):
    
    idGer = getGerAct()
    
    ger = Gerentes.objects.filter(idGerente = idGer).first()
    nombreGer = ger.nombreGer if ger else "No asignado"
    
    res = Restaurantes.objects.filter(idGerente =  idGer).first()
    nomRes = res.nombreRes if res else "No asignado"
    idRes = res.idRestaurante if res else "0"

    clientes = Clientes.objects.filter(idRestaurante = idRes)
    
    form = opBuscarCliente()
    
    
    return render(request, 'html/modificarCli.html', {
        'clientes': clientes,
        'nombre_gerente': nombreGer,
        'nomRes': nomRes,
        'opBusqueda': form,
    })