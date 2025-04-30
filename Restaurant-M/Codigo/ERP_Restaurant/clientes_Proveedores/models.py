from django.db import models
from account.models import Restaurantes

# Tabla de los clientes
class Clientes(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombreCli = models.CharField(max_length=45, null=False, blank=False)
    cedulaCli = models.IntegerField(null=False, blank=False, unique=True)
    emailCli = models.EmailField(max_length=45, null=False, blank=False, unique=True)
    telefonoCli = models.IntegerField(null=False, blank=False)
    idRestaurante = models.IntegerField(models.ForeignKey(Restaurantes, on_delete=models.DO_NOTHING, db_column='idRestaurante'), null=False)
    
    class Meta:
        managed = True
        db_table = 'Clientes'
        
    def _str_(self):
        return f"{self.nombreCli}"