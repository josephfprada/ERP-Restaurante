from django.shortcuts import render
from account.views import getGerenteAct
from account.models import Gerentes, Restaurantes

# Vista de la pagina principal del modulo de clientes y proveedores
def vistaModCliPro(request):
    idGer = getGerenteAct()
    
    ger = Gerentes.objects.filter(idGerente = idGer).first()

    nombreGer = ger.nombreGer if ger else "No asignado"
    
    res = Restaurantes.objects.filter(idGerente =  idGer).first()
    nomRes = res.nombreRes if res else "No asignado"
    
    print(nomRes)

    return render(request, 'html/homeCli.html', {
        'nombre_gerente': nombreGer,
        'nomRes': nomRes
    })