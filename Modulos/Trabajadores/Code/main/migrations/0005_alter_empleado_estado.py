# Generated by Django 5.2.1 on 2025-05-28 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_asistencia_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='estado',
            field=models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo'), ('capacitacion', 'En Capacitacion')], default='inactivo', max_length=20),
        ),
    ]
