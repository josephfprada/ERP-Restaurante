from django import forms
from .models import Empleado

class registrarEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'idEmpleado': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 1234567890'
            }),
            'nombreEmpleado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Larim Loremsum'
            }),
            'apellidoEmpleado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Falerum Astrum'
            }),
            'fechaNacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'direccionEmpleado': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Calle X, Avenida Y, Casa Z'
            }),
            'telefonoEmpleado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: +571234567890'
            }),
            'emailEmpleado': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: correo@ejemplo.es'
            }),
            'fecha_ingreso': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'puestoEmpleado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Mesero'
            }),
            'salarioEmpleado': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 1500000'
            }),
            'estado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Activo - Inactivo'
            }),
        }