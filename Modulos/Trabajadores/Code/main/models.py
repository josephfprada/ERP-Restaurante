from django.db import models

# Create your models here.

class Empleado(models.Model):

    PUESTOS = {
        (1,'Chef'),
        (2,'Cocinero'),
        (3,'Ayudante - cocina'),
        (4,'Lavaplatos'),
        (5,'Mesero'),
        (6,'Cajero'),
        (7,'Limpieza'),
    }

    ESTADO = {
        ('activo','Activo'),
        ('inactivo','Inactivo'),
        ('e.cap','En Capacitacion'),
    }

    SALARIOS_POR_PUESTO = {
        1: 3000000,  # Chef
        2: 2500000,  # Cocinero
        3: 1800000,  # Ayudante - cocina
        4: 1500000,  # Lavaplatos
        5: 2000000,  # Mesero
        6: 2200000,  # Cajero
        7: 1600000,  # Limpieza
    }

    idEmpleado = models.AutoField(primary_key=True)  # Llave primaria
    nombreEmpleado = models.CharField(max_length=100, null=False, blank=False)
    apellidoEmpleado = models.CharField(max_length=100, null=False, blank=False)
    fechaNacimiento = models.DateField(null=False, blank=False)
    direccionEmpleado = models.CharField(max_length=300, null=False, blank=False)
    telefonoEmpleado = models.CharField(max_length=17, null=False, blank=False)
    emailEmpleado = models.EmailField(max_length=100, null=False, blank=False)
    fecha_ingreso = models.DateField(null=False, blank=False)
    integer_selection = models.IntegerField(
        choices=PUESTOS,
    )
    salarioEmpleado = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    estado = models.CharField(
        max_length=8,
        choices=ESTADO,
    )
    
    class Meta:
        managed = True
        db_table = 'Empleado' 

    def __str__(self):
        return f"{self.nombreEmpleado} {self.apellidoEmpleado}"

class Asistencia(models.Model):
    idAsistencia = models.AutoField(primary_key=True)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, db_column='idEmpleado')
    entrada = models.TimeField(null=False, blank=False)
    salida = models.TimeField(null=True, blank=True)
    dia_trabajo = models.DateField(null=True, blank=True)
    estado = models.TextField(null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'Asistencia'

    def __str__(self):
        return f"Asistencia de {self.idEmpleado} - {self.dia_trabajo}"
    
class Beneficios(models.Model):
    idBeneficios = models.AutoField(primary_key=True) # Llave primaria 'idBeneficios'
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE) # Llave foranea 'idEmpleado'
    tipo_beneficio = models.CharField(max_length=45, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'Beneficios'

    def __str__(self):
        return f"{self.tipo_beneficio} ({self.idEmpleado})"
    
class Capacitacion(models.Model):
    idCapacitacion = models.AutoField(primary_key=True)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, db_column='idEmpleado')
    nombre_curso = models.CharField(max_length=255, null=False, blank=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    Calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'Capacitacion'

    def __str__(self):
        return f"{self.nombre_curso} ({self.idEmpleado})"

class Departamento(models.Model):
    idDepartamento = models.AutoField(primary_key=True) # Llave primaria 'idDepartamento'
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'Departamento'

    def __str__(self):
        return self.nombre
    
class Desempeno(models.Model):
    idDesempeno = models.AutoField(primary_key=True)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, db_column='idEmpleado')
    fecha_evaluacion = models.DateField(null=False, blank=False)
    Evaluador = models.CharField(max_length=100, null=False, blank=False)
    Calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    Comentarios = models.TextField(null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'Desempeño'

    def __str__(self):
        return f"Evaluación de {self.idEmpleado} - {self.fecha_evaluacion}"

class Documentos(models.Model):
    idDocumentos = models.AutoField(primary_key=True)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, db_column='idEmpleado')
    tipo_documento = models.CharField(max_length=45, null=False, blank=False)
    fecha_actualizacion = models.DateField(null=False, blank=False)
    documento_path = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'Documentos'

    def __str__(self):
        return f"{self.tipo_documento} - {self.idEmpleado}"
    
class EmpleadoDepartamento(models.Model):
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, db_column='idEmpleado')
    idDepartamento = models.ForeignKey('Departamento', on_delete=models.DO_NOTHING, db_column='idDepartamento')

    class Meta:
        managed = True
        db_table = 'empleado_departamento'

    def __str__(self):
        return f"{self.idEmpleado} - {self.idDepartamento}"
    
class Pago(models.Model):
    idPagos = models.AutoField(primary_key=True)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING, db_column='idEmpleado', null=True, blank=True)
    Salario = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    Bonos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Impuestos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Salario_neto = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    Inicio_periodo_pago = models.DateField(null=False, blank=False)
    Fin_periodo_pago = models.DateField(null=True, blank=True)
    Fecha_pago = models.DateField(null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'Pago'

    def __str__(self):
        return f"Pago {self.idPagos} - {self.Fecha_pago}"
    
class Permiso(models.Model):
    idPermiso = models.AutoField(primary_key=True) # Llave primaria 'idEmpidPermiso'
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE) # Llave foranea 'idEmpleado'
    tipo_permiso = models.CharField(max_length=45, null=False, blank=False)
    Permisocol = models.CharField(max_length=45, null=False, blank=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'Permiso'

    def __str__(self):
        return f"{self.tipo_permiso} - {self.idEmpleado}"

class PosicionLaboral(models.Model):
    idPosicion = models.AutoField(primary_key=True) # Llave primaria 'idRelacion'
    Puesto_trabajo = models.CharField(max_length=100, null=False, blank=False) # Llave foranea 'idEmpleado'
    IdDepartamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING, db_column='IdDepartamento')
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'Posicion_Laboral'

    def __str__(self):
        return f"{self.Puesto_trabajo} - {self.IdDepartamento}"
    
