
Este archivo es para entender como funciona Django:

// Pasos a iniciara, leer primero antes de hacer algo
Primero, si no tienes django descargado en tu computador escibe en la terminal o en el cmd "py -m pip install Django==5.2"
Segundo, para iniciar un proyecto se escribe dentro de la carpeta del proyecto en la terminal "django-admin startproject 'nomProyecto'"
Tercero, para iniciar las app del proyecto escribimos "py manage.py startapp 'nomApp'"

Las app se pueden ver a la izquierda son: "accoubt", "clientes_Proveedores" y "Recursos_Humanos"

Al querer probar el proyecto escribimos "py manage.py runserver"

// Es importante que el directorio en el que estamos tenga acceso directo al archivo "manage.py"

El archivo manage.py no se toca.


// Carpeta "ERP_Restaurant"

La carpeta "ERP_Restaurant" es por así decirlo la principal, abrimos "setting.py".
Luego en la misma carpeta abrimos "urls.py" (nota: cada app tiene su propio archivo "urls.py")

// App "account"
Podemos ver que tiene mas archivos que la carpeta anterior, empecemos por "urls.py"
Ahora vamos al arhivo "views.py"
Despues al "foms.py"
y por ultimo al "models.py"

Django funciona con un patron de diseño similar al MVC, solo que aqui es MTC (Modelo Template Controlador)

De ahí que los archivos html esten en la carpeta "Templates".
Si necesitas usar css externo, imagenes o javaScript externo, guardalos en una carpeta "static" (si las iamgens varian en tiempo
 de ejecución, preguntale a ChatGpt que hacer, solo se que es diferente)

Todo lo que este entre dos llaves "{{ algo }}", es parte del código de django, suele estar en imagens, links, llamados a css y 
 javaScript, valores a mostrar, formularios, entre otros.

No creo que necesite gran explicación.