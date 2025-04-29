from django import forms
from .models import Empleado
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.core.exceptions import ValidationError
from datetime import date, timedelta

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
                'placeholder': 'Ej: +57 3207553890'
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

def validar_mayor_de_edad(value):
    hoy = date.today()
    edad_minima = hoy - timedelta(days=18*365.25)  # Consideramos años bisiestos
    if value > edad_minima:
        raise ValidationError('El empleado debe ser mayor de 18 años.')