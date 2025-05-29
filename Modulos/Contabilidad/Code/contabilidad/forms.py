from django import forms
from .models import Factura, ComprobanteMaestro, TipoCuenta, CuentaMayor, SubCuenta, Comprobante

class FacturaForm(forms.ModelForm):
    fecha_factura = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Fecha de Factura"
    )
    fecha_vencimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False,
        label="Fecha de Vencimiento"
    )

    class Meta:
        model = Factura
        fields = [
            'numero_factura',
            'fecha_factura',
            'fecha_vencimiento',
            'tipo_factura',
            'nombre_cliente_proveedor',
            'monto_total',
            'monto_impuestos',
            'moneda',
            'estado',
            'descripcion',

        ]

        labels = {
            'numero_factura': 'Número de Factura',
            'tipo_factura': 'Tipo de Factura',
            'nombre_cliente_proveedor': 'Nombre Cliente/Proveedor',
            'monto_total': 'Monto Total',
            'monto_impuestos': 'Monto de Impuestos',
            'moneda': 'Moneda',
            'estado': 'Estado',
            'descripcion': 'Descripción',
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-control'})

class TipoCuentaForm(forms.ModelForm):
    class Meta:
        model = TipoCuenta
        fields = ['nombre', 'naturaleza_cuenta']
        labels = {
            'nombre': 'Nombre del Tipo de Cuenta',
            'naturaleza_cuenta': 'Naturaleza de la Cuenta',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'naturaleza_cuenta': forms.Select(attrs={'class': 'form-control'}),
        }

class CuentaMayorForm(forms.ModelForm):
    class Meta:
        model = CuentaMayor
        fields = ['codigo_cuenta', 'nombre_cuenta', 'tipo_cuenta']
        labels = {
            'codigo_cuenta': 'Código de Cuenta Mayor', 
            'nombre_cuenta': 'Nombre de Cuenta Mayor',
            'tipo_cuenta': 'Tipo de Cuenta (Activo, Pasivo, etc.)',
        }
        widgets = {
            'codigo_cuenta': forms.TextInput(attrs={'class': 'form-control'}), 
            'nombre_cuenta': forms.TextInput(attrs={'class': 'form-control'}), 
            'tipo_cuenta': forms.Select(attrs={'class': 'form-control'}),
        }

class SubCuentaForm(forms.ModelForm):
    class Meta:
        model = SubCuenta

        fields = ['codigo_sub_cuenta', 'nombre_sub_cuenta', 'cuenta_mayor'] 
        labels = {
            'codigo_sub_cuenta': 'Código de Sub-Cuenta',
            'nombre_sub_cuenta': 'Nombre de Sub-Cuenta',
            'cuenta_mayor': 'Cuenta Mayor a la que pertenece',
        }
        widgets = {
            'codigo_sub_cuenta': forms.TextInput(attrs={'class': 'form-control'}), 
            'nombre_sub_cuenta': forms.TextInput(attrs={'class': 'form-control'}), 
            'cuenta_mayor': forms.Select(attrs={'class': 'form-control'}),
        }

class ComprobanteForm(forms.ModelForm):
    class Meta:
        model = Comprobante
        fields = ['factura', 'tipo_comprobante', 'descripcion', 'archivo']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'factura' in self.fields:
            self.fields['factura'].queryset = Factura.objects.all().order_by('-fecha_factura')