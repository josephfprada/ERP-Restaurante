from main.models import Empleado

def run():
    empleados_data = [
        {
            'nombreEmpleado': 'Ana', 'apellidoEmpleado': 'Pérez', 'fechaNacimiento': '1990-05-15',
            'direccionEmpleado': 'Calle Falsa 123', 'telefonoEmpleado': '123-456-7890', 'emailEmpleado': 'ana.perez@example.com',
            'fecha_ingreso': '2023-01-10', 'salario': 'cajero', 'estado': 'activo', 'puesto': 'cajero'
        },
        {
            'nombreEmpleado': 'Carlos', 'apellidoEmpleado': 'López', 'fechaNacimiento': '1985-12-20',
            'direccionEmpleado': 'Avenida Siempre Viva 742', 'telefonoEmpleado': '987-654-3210', 'emailEmpleado': 'carlos.lopez@example.com',
            'fecha_ingreso': '2022-08-15', 'salario': 'cocinero', 'estado': 'activo', 'puesto': 'cocinero'
        },
        {
            'nombreEmpleado': 'Sofía', 'apellidoEmpleado': 'Gómez', 'fechaNacimiento': '1995-08-03',
            'direccionEmpleado': 'Carrera 5 # 10-20', 'telefonoEmpleado': '555-123-4567', 'emailEmpleado': 'sofia.gomez@example.com',
            'fecha_ingreso': '2024-03-01', 'salario': 'mesero', 'estado': 'inactivo', 'puesto': 'mesero'
        },
        {
            'nombreEmpleado': 'Javier', 'apellidoEmpleado': 'Ruiz', 'fechaNacimiento': '1988-03-25',
            'direccionEmpleado': 'Diagonal 30 # 2-50', 'telefonoEmpleado': '333-987-6543', 'emailEmpleado': 'javier.ruiz@example.com',
            'fecha_ingreso': '2021-05-20', 'salario': 'chef', 'estado': 'activo', 'puesto': 'chef'
        },
        {
            'nombreEmpleado': 'Elena', 'apellidoEmpleado': 'Vargas', 'fechaNacimiento': '1992-11-01',
            'direccionEmpleado': 'Transversal 1 # 4-80', 'telefonoEmpleado': '777-111-2233', 'emailEmpleado': 'elena.vargas@example.com',
            'fecha_ingreso': '2023-11-01', 'salario': 'ayudante', 'estado': 'capacitacion', 'puesto': 'ayudante'
        },
        {
            'nombreEmpleado': 'Martín', 'apellidoEmpleado': 'Soto', 'fechaNacimiento': '1991-07-10',
            'direccionEmpleado': 'Calle 20 # 15-30', 'telefonoEmpleado': '444-555-6677', 'emailEmpleado': 'martin.soto@example.com',
            'fecha_ingreso': '2022-09-01', 'salario': 'bartender', 'estado': 'activo', 'puesto': 'mesero'
        },
        {
            'nombreEmpleado': 'Isabela', 'apellidoEmpleado': 'Castro', 'fechaNacimiento': '1993-01-22',
            'direccionEmpleado': 'Avenida 40 # 5-10', 'telefonoEmpleado': '222-333-4455', 'emailEmpleado': 'isabela.castro@example.com',
            'fecha_ingreso': '2023-04-05', 'salario': 'cajero', 'estado': 'activo', 'puesto': 'cajero'
        },
        {
            'nombreEmpleado': 'Daniel', 'apellidoEmpleado': 'Torres', 'fechaNacimiento': '1987-09-05',
            'direccionEmpleado': 'Carrera 100 # 25-40', 'telefonoEmpleado': '111-222-3344', 'emailEmpleado': 'daniel.torres@example.com',
            'fecha_ingreso': '2021-12-15', 'salario': 'cocinero', 'estado': 'activo', 'puesto': 'cocinero'
        },
        {
            'nombreEmpleado': 'Valeria', 'apellidoEmpleado': 'Díaz', 'fechaNacimiento': '1994-04-18',
            'direccionEmpleado': 'Diagonal 50 # 30-50', 'telefonoEmpleado': '666-777-8899', 'emailEmpleado': 'valeria.diaz@example.com',
            'fecha_ingreso': '2024-01-20', 'salario': 'mesero', 'estado': 'activo', 'puesto': 'mesero'
        },
        {
            'nombreEmpleado': 'Mateo', 'apellidoEmpleado': 'Ortiz', 'fechaNacimiento': '1989-06-30',
            'direccionEmpleado': 'Transversal 80 # 45-60', 'telefonoEmpleado': '999-000-1122', 'emailEmpleado': 'mateo.ortiz@example.com',
            'fecha_ingreso': '2022-06-01', 'salario': 'chef', 'estado': 'activo', 'puesto': 'chef'
        },
        {
            'nombreEmpleado': 'Lucía', 'apellidoEmpleado': 'Jiménez', 'fechaNacimiento': '1996-10-12',
            'direccionEmpleado': 'Calle 5 # 7-90', 'telefonoEmpleado': '333-444-5566', 'emailEmpleado': 'lucia.jimenez@example.com',
            'fecha_ingreso': '2023-07-10', 'salario': 'ayudante', 'estado': 'activo', 'puesto': 'ayudante'
        },
        {
            'nombreEmpleado': 'Sebastián', 'apellidoEmpleado': 'Núñez', 'fechaNacimiento': '1990-12-08',
            'direccionEmpleado': 'Avenida 68 # 12-34', 'telefonoEmpleado': '777-888-9900', 'emailEmpleado': 'sebastian.nunez@example.com',
            'fecha_ingreso': '2022-11-01', 'salario': 'bartender', 'estado': 'activo', 'puesto': 'mesero'
        },
        {
            'nombreEmpleado': 'Camila', 'apellidoEmpleado': 'Flores', 'fechaNacimiento': '1997-02-14',
            'direccionEmpleado': 'Carrera 7 # 50-70', 'telefonoEmpleado': '222-999-1133', 'emailEmpleado': 'camila.flores@example.com',
            'fecha_ingreso': '2024-02-15', 'salario': 'cajero', 'estado': 'activo', 'puesto': 'cajero'
        },
        {
            'nombreEmpleado': 'Andrés', 'apellidoEmpleado': 'Méndez', 'fechaNacimiento': '1986-07-28',
            'direccionEmpleado': 'Diagonal 79 # 1-15', 'telefonoEmpleado': '555-000-2244', 'emailEmpleado': 'andres.mendez@example.com',
            'fecha_ingreso': '2021-09-01', 'salario': 'cocinero', 'estado': 'activo', 'puesto': 'cocinero'
        },
        {
            'nombreEmpleado': 'Mariana', 'apellidoEmpleado': 'Rojas', 'fechaNacimiento': '1993-09-21',
            'direccionEmpleado': 'Transversal 5 # 33-55', 'telefonoEmpleado': '888-111-3355', 'emailEmpleado': 'mariana.rojas@example.com',
            'fecha_ingreso': '2023-05-10', 'salario': 'mesero', 'estado': 'activo', 'puesto': 'mesero'
        },
        {
            'nombreEmpleado': 'Nicolás', 'apellidoEmpleado': 'Silva', 'fechaNacimiento': '1988-11-07',
            'direccionEmpleado': 'Calle 10 # 22-44', 'telefonoEmpleado': '111-444-7788', 'emailEmpleado': 'nicolas.silva@example.com',
            'fecha_ingreso': '2022-03-15', 'salario': 'chef', 'estado': 'activo', 'puesto': 'chef'
        },
        {
            'nombreEmpleado': 'Gabriela', 'apellidoEmpleado': 'Vega', 'fechaNacimiento': '1991-03-09',
            'direccionEmpleado': 'Avenida 3 # 60-80', 'telefonoEmpleado': '666-999-3300', 'emailEmpleado': 'gabriela.vega@example.com',
            'fecha_ingreso': '2023-09-20', 'salario': 'ayudante', 'estado': 'activo', 'puesto': 'ayudante'
        },
        {
            'nombreEmpleado': 'Santiago', 'apellidoEmpleado': 'Pinto', 'fechaNacimiento': '1995-05-02',
            'direccionEmpleado': 'Carrera 55 # 10-30', 'telefonoEmpleado': '999-222-5511', 'emailEmpleado': 'santiago.pinto@example.com',
            'fecha_ingreso': '2024-01-05', 'salario': 'bartender', 'estado': 'activo', 'puesto': 'mesero'
        },
        {
            'nombreEmpleado': 'Emilia', 'apellidoEmpleado': 'Blanco', 'fechaNacimiento': '1998-01-17',
            'direccionEmpleado': 'Diagonal 20 # 40-60', 'telefonoEmpleado': '333-666-9922', 'emailEmpleado': 'emilia.blanco@example.com',
            'fecha_ingreso': '2023-12-01', 'salario': 'cajero', 'estado': 'activo', 'puesto': 'cajero'
        },
        {
            'nombreEmpleado': 'Felipe', 'apellidoEmpleado': 'Guerrero', 'fechaNacimiento': '1987-04-29',
            'direccionEmpleado': 'Transversal 10 # 15-35', 'telefonoEmpleado': '777-000-4433', 'emailEmpleado': 'felipe.guerrero@example.com',
            'fecha_ingreso': '2022-07-15', 'salario': 'cocinero', 'estado': 'activo', 'puesto': 'cocinero'
        },
        {
            'nombreEmpleado': 'Renata', 'apellidoEmpleado': 'Zapata', 'fechaNacimiento': '1994-08-11',
            'direccionEmpleado': 'Calle 30 # 5-25', 'telefonoEmpleado': '222-555-8844', 'emailEmpleado': 'renata.zapata@example.com',
            'fecha_ingreso': '2023-03-20', 'salario': 'mesero', 'estado': 'activo', 'puesto': 'mesero'
        },
        {
            'nombreEmpleado': 'Joaquín', 'apellidoEmpleado': 'Herrera', 'fechaNacimiento': '1989-12-23',
            'direccionEmpleado': 'Avenida 70 # 30-50', 'telefonoEmpleado': '555-888-1155', 'emailEmpleado': 'joaquin.herrera@example.com',
            'fecha_ingreso': '2021-11-01', 'salario': 'chef', 'estado': 'activo', 'puesto': 'chef'
        },
        {
            'nombreEmpleado': 'Antonella', 'apellidoEmpleado': 'Sánchez', 'fechaNacimiento': '1992-06-04',
            'direccionEmpleado': 'Carrera 15 # 20-40', 'telefonoEmpleado': '888-333-6677', 'emailEmpleado': 'antonella.sanchez@example.com',
            'fecha_ingreso': '2022-10-10', 'salario': 'ayudante', 'estado': 'activo', 'puesto': 'ayudante'
        },
        {
            'nombreEmpleado': 'Benjamín', 'apellidoEmpleado': 'Ramírez', 'fechaNacimiento': '1996-09-16',
            'direccionEmpleado': 'Diagonal 40 # 1-10', 'telefonoEmpleado': '111-666-9988', 'emailEmpleado': 'benjamin.ramirez@example.com',
            'fecha_ingreso': '2024-03-05', 'salario': 'bartender', 'estado': 'activo', 'puesto': 'mesero'
        },
        {
            'nombreEmpleado': 'Monserrat', 'apellidoEmpleado': 'Cruz', 'fechaNacimiento': '1999-03-01',
            'direccionEmpleado': 'Transversal 20 # 50-70', 'telefonoEmpleado': '666-111-4499', 'emailEmpleado': 'monserrat.cruz@example.com',
            'fecha_ingreso': '2023-06-20', 'salario': 'cajero', 'estado': 'activo', 'puesto': 'cajero'
        },
        {
            'nombreEmpleado': 'Cristóbal', 'apellidoEmpleado': 'Fuentes', 'fechaNacimiento': '1985-11-27',
            'direccionEmpleado': 'Calle 45 # 7-30', 'telefonoEmpleado': '999-444-7700', 'emailEmpleado': 'cristobal.fuentes@example.com',
            'fecha_ingreso': '2021-08-01', 'salario': 'cocinero', 'estado': 'activo', 'puesto': 'cocinero'
        },
        {
            'nombreEmpleado': 'Agustina', 'apellidoEmpleado': 'Valdés', 'fechaNacimiento': '1993-07-19',
            'direccionEmpleado': 'Avenida 5 # 22-44', 'telefonoEmpleado': '333-777-0011', 'emailEmpleado': 'agustina.valdes@example.com',
            'fecha_ingreso': '2022-12-10', 'salario': 'mesero', 'estado': 'activo', 'puesto': 'mesero'
        },
        {
            'nombreEmpleado': 'Vicente', 'apellidoEmpleado': 'Morales', 'fechaNacimiento': '1988-02-10',
            'direccionEmpleado': 'Carrera 80 # 1-15', 'telefonoEmpleado': '777-222-5522', 'emailEmpleado': 'vicente.morales@example.com',
            'fecha_ingreso': '2023-01-15', 'salario': 'chef', 'estado': 'activo', 'puesto': 'chef'
        },
        {
            'nombreEmpleado': 'Catalina', 'apellidoEmpleado': 'Navarro', 'fechaNacimiento': '1990-08-22',
            'direccionEmpleado': 'Diagonal 60 # 30-50', 'telefonoEmpleado': '222-666-9933', 'emailEmpleado': 'catalina.navarro@example.com',
            'fecha_ingreso': '2022-05-01', 'salario': 'ayudante', 'estado': 'activo', 'puesto': 'ayudante'
        },
        {
            'nombreEmpleado': 'Maximiliano', 'apellidoEmpleado': 'Reyes', 'fechaNacimiento': '1997-06-05',
            'direccionEmpleado': 'Transversal 30 # 5-25', 'telefonoEmpleado': '555-999-2244', 'emailEmpleado': 'maximiliano.reyes@example.com',
            'fecha_ingreso': '2024-03-25', 'salario': 'bartender', 'estado': 'activo', 'puesto': 'mesero'
        }
    ]

    for data in empleados_data:
        try:
            Empleado.objects.create(**data)
        except Exception as e:
            print(f"Error al crear empleado con datos: {data}. Error: {e}")

    print(f"{len(empleados_data)} empleados agregados.")