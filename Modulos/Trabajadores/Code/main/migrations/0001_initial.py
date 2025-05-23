# Generated by Django 5.2 on 2025-04-21 00:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('idDepartamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'Departamento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombreEmpleado', models.CharField(max_length=100)),
                ('apellidoEmpleado', models.CharField(max_length=100)),
                ('fechaNacimiento', models.DateField()),
                ('direccionEmpleado', models.CharField(max_length=300)),
                ('telefonoEmpleado', models.CharField(max_length=15)),
                ('emailEmpleado', models.EmailField(max_length=100)),
                ('fecha_ingreso', models.DateField()),
                ('puestoEmpleado', models.CharField(max_length=100)),
                ('salarioEmpleado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'Empleado',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('idDocumentos', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_documento', models.CharField(max_length=45)),
                ('fecha_actualizacion', models.DateField()),
                ('documento_path', models.CharField(max_length=255)),
                ('idEmpleado', models.ForeignKey(db_column='idEmpleado', on_delete=django.db.models.deletion.DO_NOTHING, to='main.empleado')),
            ],
            options={
                'db_table': 'Documentos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Desempeno',
            fields=[
                ('idDesempeno', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_evaluacion', models.DateField()),
                ('Evaluador', models.CharField(max_length=100)),
                ('Calificacion', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Comentarios', models.TextField()),
                ('idEmpleado', models.ForeignKey(db_column='idEmpleado', on_delete=django.db.models.deletion.DO_NOTHING, to='main.empleado')),
            ],
            options={
                'db_table': 'Desempeño',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('idCapacitacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_curso', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('Calificacion', models.DecimalField(decimal_places=2, max_digits=5)),
                ('idEmpleado', models.ForeignKey(db_column='idEmpleado', on_delete=django.db.models.deletion.DO_NOTHING, to='main.empleado')),
            ],
            options={
                'db_table': 'Capacitacion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Beneficios',
            fields=[
                ('idBeneficios', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_beneficio', models.CharField(max_length=45)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.empleado')),
            ],
            options={
                'db_table': 'Beneficios',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('idAsistencia', models.AutoField(primary_key=True, serialize=False)),
                ('entrada', models.TimeField()),
                ('salida', models.TimeField(blank=True, null=True)),
                ('dia_trabajo', models.DateField(blank=True, null=True)),
                ('estado', models.TextField()),
                ('idEmpleado', models.ForeignKey(db_column='idEmpleado', on_delete=django.db.models.deletion.DO_NOTHING, to='main.empleado')),
            ],
            options={
                'db_table': 'Asistencia',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmpleadoDepartamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDepartamento', models.ForeignKey(db_column='idDepartamento', on_delete=django.db.models.deletion.DO_NOTHING, to='main.departamento')),
                ('idEmpleado', models.ForeignKey(db_column='idEmpleado', on_delete=django.db.models.deletion.DO_NOTHING, to='main.empleado')),
            ],
            options={
                'db_table': 'empleado_departamento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('idPagos', models.AutoField(primary_key=True, serialize=False)),
                ('Salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Bonos', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Impuestos', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Salario_neto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Inicio_periodo_pago', models.DateField()),
                ('Fin_periodo_pago', models.DateField(blank=True, null=True)),
                ('Fecha_pago', models.DateField()),
                ('idEmpleado', models.ForeignKey(blank=True, db_column='idEmpleado', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.empleado')),
            ],
            options={
                'db_table': 'Pago',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('idPermiso', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_permiso', models.CharField(max_length=45)),
                ('Permisocol', models.CharField(max_length=45)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.empleado')),
            ],
            options={
                'db_table': 'Permiso',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PosicionLaboral',
            fields=[
                ('idPosicion', models.AutoField(primary_key=True, serialize=False)),
                ('Puesto_trabajo', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('IdDepartamento', models.ForeignKey(db_column='IdDepartamento', on_delete=django.db.models.deletion.DO_NOTHING, to='main.departamento')),
            ],
            options={
                'db_table': 'Posicion_Laboral',
                'managed': True,
            },
        ),
    ]
