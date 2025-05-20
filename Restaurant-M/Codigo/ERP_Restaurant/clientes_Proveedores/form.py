from django import forms
from .models import Restaurantes, Clientes
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.core.exceptions import ValidationError
from datetime import date, timedelta

# Registro del restaurante
class registrarCliente(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
        widgets = {
            'idCliente': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 1234567890'
            }),
            'nombreCli': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Pedro Pascal'
            }),
            'telefonoCli': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 3152089870'
            }),
            'cedulaCli': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 107878768'
            }),
            'emailCli': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: PP@email.com'
            }),
            'idRestaurante': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Revisar valor'
            })}
        
        labels = {
            'nombreCli': 'Nombre del Cliente*:',
            'telefonoCli': 'Numero de Teléfono*:',
            'cedulaCli': 'Cédula del Cliente:',
            'emailCli': 'Email del Cliente:',
            'idRestaurante': 'ID del Restaurante*:',
        }

# Buscador del cliente
class opBuscarCliente(forms.Form):
    class Meta:
        opBusqueda = [
            ('nombreCli', 'Nombre'),
            ('cedulaCli', 'Cédula'),
            ('emailCli', 'Email'),
            ('telefonoCli', 'Teléfono'),
        ]
        
        buscaCliente = forms.ChoiceField(
            choices = opBusqueda,
            label = "Seleccionar opción",
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        
