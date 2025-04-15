#Instalar Django antes de ejecución
#   python -m pip show django   -->   python -m pip install django

#Importancion de modelos respecto a la DBB (MySQL)
from django.db import models

#Definicion de departamento
class Departamento(models.Model):
    idDepartamento = models.AutoField(primary_key=True) # Llave primaria 'idDepartamento'
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        managed = False  # Evita que Django manipule las tablas
        db_table = 'Departamento' 

    def __str__(self):
        return self.nombre

# Instanciamiento de los campos por empleado
class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True) # Llave pimaria 'idEmpleado'
    nombreEmpleado = models.CharField(max_length=100, null=False, blank=False)
    fechaNacimiento = models.DateField(null=False, blank=False)
    direccionEmpleado = models.CharField(max_length=300, null=False, blank=False)
    telefonoEmpleado = models.CharField(max_length=12, null=False, blank=False)
    fecha_ingreso = models.DateTimeField(null=False, blank=False)
    puestoEmpleado = models.CharField(max_length=100, null=False, blank=False)
    salarioEmpleado = models.DecimalField(max_digits=10, null=False, blank=False)
    estado = models.CharField(max_length=8, null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'Empleado' 

    def __str__(self):
        return f"{self.nombreEmpleado} {self.apellidoEmpleado}"
    
# Relacion empleado-departamento
class EmpleadoDepartamento(models.Model):
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE) # Llave primaria 'idEmpleado'
    idDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE) # Llave foranea 'idDepartamento'

    class Meta:
        managed = False
        unique_together = ('idEmpleado', 'idDepartamento')

# Instanciamiento de la estructura capacitaciones
class Capacitacion(models.Model):
    idCapacitacion = models.AutoField(primary_key=True) # Llave foranea 'idCapacitacion'
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE) # Llave foranea 'idEmpleado'
    nombre_curso = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    calificacion = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Capacitacion'

    def __str__(self):
        return self.nombre_curso

# Definicion de los beneficios - empleados
class Beneficios(models.Model):
    idBeneficios = models.AutoField(primary_key=True) # Llave primaria 'idBeneficios'
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE) # Llave foranea 'idEmpleado'
    tipo_beneficio = models.CharField(max_length=45)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        managed = False
        db_table = 'Beneficios'

    def __str__(self):
        return self.tipo_beneficio

# Metodo de calificacion - empleados
class Desempeno(models.Model):
    idDesempeño = models.AutoField(primary_key=True) # Llave primaria 'idDesempeño'
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE) # Llave foranea 'idEmpleado'
    fecha_evaluacion = models.DateField()
    evaluador = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)
    comentarios = models.TextField()

    class Meta:
        managed = False
        db_table = 'Desempeno'

    def __str__(self):
        return f"Evaluación de {self.idEmpleado}"

# Manejo de permisos - empleados
class Permiso(models.Model):
    idPermiso = models.AutoField(primary_key=True) # Llave primaria 'idEmpidPermiso'
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE) # Llave foranea 'idEmpleado'
    tipo_permiso = models.CharField(max_length=45)
    permisocol = models.CharField(max_length=45)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        managed = False
        db_table = 'Permiso'

    def __str__(self):
        return self.tipo_permiso

# Emplazamiento laboral
class RelacionLaboral(models.Model):
    idRelacion = models.AutoField(primary_key=True) # Llave primaria 'idRelacion'
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE) # Llave foranea 'idEmpleado'
    tipo_relacion = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()   
    fecha_fin = models.DateField()

    class Meta:
        managed = False
        db_table = 'RelacionLaboral'

    def __str__(self):
        return self.tipo_relacion
    
