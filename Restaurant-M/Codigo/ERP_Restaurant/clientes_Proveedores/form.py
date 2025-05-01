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
            'cedulaCli': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 107878768'
            }),
            'emailCli': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: PP@email.com'
            }),
            'telefonoCli': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 3152089870'
            }),
            'idRestaurante': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Revisar valor'
            })}
        
        labels = {
            'idRestaurante': 'ID del Restaurante:',
            'nombreRes': 'Nombre del Restaurante:',
            'direccionRes': 'Dirección:',
            'idGerente': 'Id del gerente',
        }