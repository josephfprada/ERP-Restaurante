from django.db import models
    
# Tabla de los gerentes
class Gerentes(models.Model):
    idGerente = models.AutoField(primary_key=True)
    nombreGer = models.CharField(max_length=45, null=False, blank=False)
    emailGer = models.EmailField(max_length=45, null=False, blank=False)
    telefonoGer = models.IntegerField( null=False, blank=False)
    passwordGer = models.CharField(max_length=45, null=False, blank=False)
    
    class Meta:
        managed = True
        db_table = 'Gerentes'
        
    def _str_(self):
        return f"{self.nombreGer}"
    
# Tabla de los restaurantes
class Restaurantes(models.Model):
    idRestaurante = models.AutoField(primary_key=True)
    nombreRes = models.CharField(max_length=45, null=False, blank=False)
    direccionRes = models.CharField(max_length=45, null=False, blank=False)
    idGerente = models.IntegerField(models.ForeignKey(Gerentes, on_delete=models.DO_NOTHING, db_column='idGerente'), null=False)
    
    class Meta:
        managed = True
        db_table = 'Restaurantes'
        
    def _str_(self):
        return f"{self.nombreRes}"