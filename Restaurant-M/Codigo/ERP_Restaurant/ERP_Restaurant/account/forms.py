from django import forms
from .models import Gerentes, Restaurantes
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.core.exceptions import ValidationError
from datetime import date, timedelta

# Registro del gerente del restaurante
class registrarGerente(forms.ModelForm):
    class Meta:
        model = Gerentes
        fields = '__all__'
        widgets = {
            'idGerente': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 1234567890'
            }),
            'nombreGer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Diego Aquino'
            }),
            'eamilGer': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: example@email.com'
            }),
            'telefonoGer': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': '3152082908'
            }),
            'passwordGer': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': '******'
            })}
        
        labels = {
            'idGerente': 'ID del Gerent:',
            'nombreGer': 'Nombre del Gerente:',
            'emailGer': 'Correo Electrónico:',
            'telefonoGer': 'Teléfono de Contacto:',
            'passwordGer': 'Contraseña:',
        }
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if Gerentes.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return email

# Registro del restaurante
class registrarRestaurante(forms.ModelForm):
    class Meta:
        model = Restaurantes
        fields = '__all__'
        ger = Gerentes.objects.last()
        widgets = {
            'idRestaurante': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 1234567890'
            }),
            'nombreRes': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Pescaderia La Mojarra'
            }),
            'direccionRes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: kr 7ta cll 64'
            }),
            'idGerentes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Revisar valor'
            })}
        
        labels = {
            'idRestaurante': 'ID del Restaurante:',
            'nombreRes': 'Nombre del Restaurante:',
            'direccionRes': 'Dirección:',
            'idGerente': 'Id del gerente',
        }

# Login a la aplicación web
class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: gerente@email.com'
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '*******'
        })
    )