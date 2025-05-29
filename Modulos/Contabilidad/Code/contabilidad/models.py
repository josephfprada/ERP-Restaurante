from django.db import models
from django.utils.translation import gettext_lazy as _



class TipoCuenta(models.Model):
    class NaturalezaCuenta(models.TextChoices):
        DEBITO = 'DEBITO', _('Débito')
        CREDITO = 'CREDITO', _('Crédito')

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Nombre del Tipo de Cuenta",
        help_text="Ej: Activo, Pasivo, Ingresos."
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción",
        help_text="Descripción detallada del tipo de cuenta."
    )
    naturaleza_cuenta = models.CharField(
        max_length=10,
        choices=NaturalezaCuenta.choices,
        verbose_name="Naturaleza de la Cuenta",
        help_text="Define si la cuenta aumenta con débitos o créditos."
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tipo de Cuenta"
        verbose_name_plural = "Tipos de Cuentas"
        ordering = ['nombre'] 

    def __str__(self):
        return self.nombre


class CuentaMayor(models.Model):

    id = models.AutoField(primary_key=True)
    codigo_cuenta = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Código de Cuenta",
        help_text="Código único para la cuenta principal (ej: 110505)."
    )
    nombre_cuenta = models.CharField(
        max_length=100,
        verbose_name="Nombre de Cuenta",
        help_text="Nombre de la cuenta principal (ej: Caja General)."
    )
    tipo_cuenta = models.ForeignKey(
        TipoCuenta,
        on_delete=models.PROTECT, 
        related_name='cuentas_mayores',
        verbose_name="Tipo de Cuenta"
    )
    esta_activa = models.BooleanField(
        default=True,
        verbose_name="¿Está Activa?",
        help_text="Indica si la cuenta está activa para transacciones."
    )
    permite_transacciones = models.BooleanField(
        default=True,
        verbose_name="¿Permite Transacciones Directas?",
        help_text="Indica si se pueden registrar transacciones directamente en esta cuenta (algunas son solo para agrupación)."
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cuenta Mayor"
        verbose_name_plural = "Cuentas Mayores"
        ordering = ['codigo_cuenta'] 

    def __str__(self):
        return f"{self.codigo_cuenta} - {self.nombre_cuenta}"


class SubCuenta(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_sub_cuenta = models.CharField( 
        max_length=20,
        unique=True,
        verbose_name="Código de Sub-Cuenta",
        help_text="Código único para la sub-cuenta (ej: 11050501)."
    )
    nombre_sub_cuenta  = models.CharField(
        max_length=100,
        verbose_name="Nombre de Sub-Cuenta",
        help_text="Nombre de la sub-cuenta (ej: Caja Menor)."
    )
    cuenta_mayor = models.ForeignKey(
        CuentaMayor,
        on_delete=models.PROTECT,
        related_name='subcuentas',
        verbose_name="Cuenta Mayor"
    )
    esta_activa = models.BooleanField(
        default=True,
        verbose_name="¿Está Activa?"
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sub-Cuenta"
        verbose_name_plural = "Sub-Cuentas"
        ordering = ['codigo_sub_cuenta']

    def __str__(self):
        return f"{self.codigo_sub_cuenta} - {self.nombre_sub_cuenta}"



class ComprobanteMaestro(models.Model):
    class TipoComprobante(models.TextChoices):
        DIARIO = 'DIARIO', _('Comprobante Diario')
        INGRESO = 'INGRESO', _('Comprobante de Ingreso')
        EGRESO = 'EGRESO', _('Comprobante de Egreso')
        TRANSFERENCIA = 'TRANSFERENCIA', _('Comprobante de Transferencia')
       

    class EstadoComprobante(models.TextChoices):
        PENDIENTE = 'PENDIENTE', _('Pendiente')
        CONTABILIZADO = 'CONTABILIZADO', _('Contabilizado')
        ANULADO = 'ANULADO', _('Anulado')
        BORRADOR = 'BORRADOR', _('Borrador')

    id = models.AutoField(primary_key=True)
    numero_comprobante = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Número de Comprobante",
        help_text="Número único generado por el sistema para el comprobante (ej: COMP00001)."
    )
    fecha_comprobante = models.DateField(
        verbose_name="Fecha del Comprobante",
        help_text="Fecha en que ocurrió la transacción."
    )
    fecha_contabilizacion = models.DateField(
        verbose_name="Fecha de Contabilización",
        help_text="Fecha en que el comprobante fue registrado en el sistema contable."
    )
    tipo_comprobante = models.CharField(
        max_length=20,
        choices=TipoComprobante.choices,
        default=TipoComprobante.DIARIO,
        verbose_name="Tipo de Comprobante"
    )
    descripcion = models.TextField(
        verbose_name="Descripción General",
        help_text="Descripción breve del propósito general del comprobante."
    )
    total_debito = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0.00,
        verbose_name="Total Débito"
    )
    total_credito = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0.00,
        verbose_name="Total Crédito"
    )
    estado = models.CharField(
        max_length=20,
        choices=EstadoComprobante.choices,
        default=EstadoComprobante.PENDIENTE,
        verbose_name="Estado del Comprobante"
    )
 
    tipo_documento_fuente = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Tipo de Documento Fuente",
        help_text="Ej: Factura, Recibo de Caja, Nómina."
    )
    id_documento_fuente = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="ID del Documento Fuente",
        help_text="ID del documento en su tabla original (ej: ID de la Factura)."
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Comprobante Contable"
        verbose_name_plural = "Comprobantes Contables"
        ordering = ['-fecha_comprobante', '-numero_comprobante'] 

    def __str__(self):
        return f"{self.numero_comprobante} ({self.fecha_comprobante})"

    def clean(self):

        from django.core.exceptions import ValidationError
        if self.total_debito != self.total_credito:
            raise ValidationError("La suma de los débitos y créditos debe ser igual en el comprobante.")

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)


class DetalleComprobante(models.Model):
    id = models.AutoField(primary_key=True)
    comprobante_maestro = models.ForeignKey(
        ComprobanteMaestro,
        on_delete=models.CASCADE, 
        related_name='detalles',
        verbose_name="Comprobante Principal"
    )
    cuenta_mayor = models.ForeignKey(
        CuentaMayor,
        on_delete=models.PROTECT,
        related_name='detalles_comprobante',
        verbose_name="Cuenta Mayor Contable"
    )
    sub_cuenta = models.ForeignKey(
        SubCuenta,
        on_delete=models.PROTECT,
        related_name='detalles_comprobante',
        blank=True,
        null=True,
        verbose_name="Sub-Cuenta Contable",
        help_text="Opcional, si la transacción afecta una sub-cuenta específica."
    )
    monto_debito = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0.00,
        verbose_name="Monto Débito"
    )
    monto_credito = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0.00,
        verbose_name="Monto Crédito"
    )
    descripcion_linea = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Descripción de la Línea",
        help_text="Descripción específica de esta parte del asiento."
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Detalle del Comprobante"
        verbose_name_plural = "Detalles del Comprobante"
        ordering = ['comprobante_maestro', 'id']

    def __str__(self):
        return f"Detalle {self.id} de {self.comprobante_maestro.numero_comprobante}"

    def clean(self):
        """
        Método de validación a nivel de modelo para el detalle del comprobante.
        """
        from django.core.exceptions import ValidationError

        if self.monto_debito > 0 and self.monto_credito > 0:
            raise ValidationError("Una línea de detalle no puede tener montos de débito y crédito al mismo tiempo.")
        if self.monto_debito == 0 and self.monto_credito == 0:
            raise ValidationError("Una línea de detalle debe tener un monto de débito o crédito.")

        if not self.cuenta_mayor.permite_transacciones:
            raise ValidationError(f"No se pueden registrar transacciones directamente en la cuenta '{self.cuenta_mayor.nombre_cuenta}'.")

        if self.sub_cuenta and self.sub_cuenta.cuenta_mayor != self.cuenta_mayor:
            raise ValidationError("La sub-cuenta seleccionada no pertenece a la cuenta mayor.")


class Factura(models.Model):
    class TipoFactura(models.TextChoices):
        VENTA = 'VENTA', _('Venta')
        COMPRA = 'COMPRA', _('Compra')

    class EstadoFactura(models.TextChoices):
        BORRADOR = 'BORRADOR', _('Borrador')
        EMITIDA = 'EMITIDA', _('Emitida')
        PAGADA = 'PAGADA', _('Pagada')
        PAGADA_PARCIALMENTE = 'PAGADA_PARCIALMENTE', _('Pagada Parcialmente')
        ANULADA = 'ANULADA', _('Anulada')

    id = models.AutoField(primary_key=True)
    numero_factura = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Número de Factura"
    )
    fecha_factura = models.DateField(
        verbose_name="Fecha de Factura"
    )
    fecha_vencimiento = models.DateField(
        verbose_name="Fecha de Vencimiento",
        blank=True,
        null=True
    )
    tipo_factura = models.CharField(
        max_length=20,
        choices=TipoFactura.choices,
        verbose_name="Tipo de Factura"
    )

    nombre_cliente_proveedor = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Nombre Cliente/Proveedor",
        help_text="Nombre del cliente o proveedor asociado a la factura."
    )

    monto_total = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        verbose_name="Monto Total"
    )
    monto_impuestos = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0.00,
        verbose_name="Monto Impuestos"
    )
    moneda = models.CharField(
        max_length=3,
        default='COP', 
        verbose_name="Moneda",
        help_text="Código ISO 4217 de la moneda (ej: COP, USD)."
    )
    estado = models.CharField(
        max_length=20,
        choices=EstadoFactura.choices,
        default=EstadoFactura.BORRADOR,
        verbose_name="Estado de Factura"
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción"
    )

    comprobante_maestro = models.OneToOneField(
        'ComprobanteMaestro',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='factura_asociada',
        verbose_name="Comprobante Contable Asociado",
        help_text="Comprobante contable generado a partir de esta factura."
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ['-fecha_factura', '-numero_factura']

    def __str__(self):
        return f"Factura {self.numero_factura} ({self.get_tipo_factura_display()})"

class Comprobante(models.Model):
    TIPO_COMPROBANTE_CHOICES = [
        ('RECIBO', 'Recibo de Pago'),
        ('NOTA_ENTREGA', 'Nota de Entrega'),
        ('JUSTIFICANTE_PAGO', 'Justificante de Pago'),
        ('OTRO', 'Otro'),
    ]

    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='comprobantes')
    tipo_comprobante = models.CharField(max_length=20, choices=TIPO_COMPROBANTE_CHOICES, default='OTRO')
    descripcion = models.TextField(blank=True, null=True, help_text="Breve descripción del comprobante.")
    archivo = models.FileField(upload_to='comprobantes/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comprobante para Factura #{self.factura.numero_factura} - {self.get_tipo_comprobante_display()}"

    class Meta:
        verbose_name = "Comprobante"
        verbose_name_plural = "Comprobantes"
        ordering = ['-fecha_subida']
