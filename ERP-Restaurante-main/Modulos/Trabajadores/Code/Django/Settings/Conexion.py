# Correr  "python manage.py inspectdb > models.py" en BASH para generar un modelo de la DB 

DATABASE = {
    'default': {
        'MOTOR': 'mysql.connector.django',
        'NOMBRE': 'ERP-HumanResources',
        'USUARIO': 'HumanResources',
        'PASSWORD': '123456789erp',
        'HOST': 'localhost',
        'PUERTO': '3306',

        # Soporte UNICODE
        'OPCIONES': {
            'charset': 'utf8'
        }
    }
}

