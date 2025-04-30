from django.shortcuts import render

# Vista de la pagina principal del modulo de clientes y proveedores
def vistaModCliPro(response):
    return render(response, 'html/homeCli.html', {})