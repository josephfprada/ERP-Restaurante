# ERP-Restaurante
Desarrollo de un ERP (Enterprise resource planning), con sus respectivas fases de desarrollo por medio de la metodologia SCRUM, implementando la herramienta Jira.

Jira link: https://s0ftw4r3arch1tectur3.atlassian.net/jira/software/projects/AER/boards/4?atlOrigin=eyJpIjoiMTA1MWFhYjczOThiNDQ2MTgwNjYzNjVhZjgyNTk3ZTkiLCJwIjoiaiJ9

Para abrir el espacio de trabajo:
1. Extrae "ERP-Restaurante-main.zip".
2. Dentro busca y extrae "restaurante_erp.zip", entra en la carpeta descomprimida.
3. Abre las carpetas hasta ver el archivo "manage.py".
4. Ya puedes trabajar en la carpeta que contenga dicho archivo.

Para correr el programa siga estos pasos:
1. Escribir en la terminal de Visual "py -m pip install Django==5.2"(si estas en windows, "python -m pip install Django==5.2" si estas en Linux), para instalar django.
2. Instale los siguientes paquetes "pip install mysql-connector-python", "pip install django-import-export".
3. Ahora vamos a crear la base de datos escribiendo "CREATE DATABASE restaurante_erp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;" en la consola de MySQL (MySQL X.X Command Line Client, en windows).
4. Por último en "restaurante_erp > restaurante_erp > settings.py", busca "'PASWWORD':'root'" y cambia la contraseña por la que tengas en el usuario "root".
5. Escribe el comando "py manage.py migrate", para crear las tablas necesarias dentro de "restaurante_erp".
6. Ahora en la terminal de Visual escribir "py manage.py runserver", para iniciar el servidor local, es IMPORTANTE tener en cuenta que que al escribir el comando tienes que estar en el diretorio que contenga al archivo "manage.py", sino no funcionara.
7. Al escribir el comando empezara a aparecera la url de prueba, manten el mouse encima y oprime "follow link" (o copia y pega la url, "https://127.0.0.1:8080/")
