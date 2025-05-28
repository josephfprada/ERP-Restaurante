from django import forms
from .models import Empleado, Documentos, EvaluacionDesempeno
from django.core.exceptions import ValidationError
from datetime import date

def validar_mayor_de_edad(value):
    hoy = date.today()
    edad = hoy.year - value.year - ((hoy.month, hoy.day) < (value.month, value.day))
    if edad < 18:
        raise ValidationError('El empleado debe ser mayor de 18 años.')

def validar_formato_telefono(value):
    if not (value.startswith('+') and value[1:].isdigit() or value.isdigit()):
        raise ValidationError('El número de teléfono debe tener el formato "+prefijo""numero" (Ej: +573207553890) o solo números.')


class RegistrarEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'nombreEmpleado',
            'apellidoEmpleado',
            'fechaNacimiento',
            'direccionEmpleado',
            'telefonoEmpleado',
            'emailEmpleado',
            'fecha_ingreso',
            'puesto',        
            'salario',      
            'estado',
        ]
        widgets = {
            'nombreEmpleado': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoEmpleado': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaNacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'direccionEmpleado': forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoEmpleado': forms.TextInput(attrs={'class': 'form-control'}),
            'emailEmpleado': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'puesto': forms.Select(attrs={'class': 'form-control'}),
            'salario': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_fechaNacimiento(self):
        fecha_nacimiento = self.cleaned_data['fechaNacimiento']
        validar_mayor_de_edad(fecha_nacimiento)
        return fecha_nacimiento

    def clean_telefonoEmpleado(self):
        telefono = self.cleaned_data['telefonoEmpleado']
        validar_formato_telefono(telefono)
        if not (10 <= len(telefono) <= 17): 
            raise ValidationError('El número de teléfono debe tener entre 10 y 17 caracteres.')
        return telefono

    def clean_emailEmpleado(self):
        email = self.cleaned_data['emailEmpleado']

        return email

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ['idEmpleado', 'tipo_documento', 'fecha_actualizacion', 'documento']
        widgets = {
            'idEmpleado': forms.Select(attrs={'class': 'form-control'}),
            'tipo_documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Hoja de Vida'}),
            'fecha_actualizacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    
class EvaluacionDesempenoForm(forms.ModelForm):
    puntuacion = forms.IntegerField(min_value=1, max_value=10, help_text="Puntuación del desempeño (1-10)")

    class Meta:
        model = EvaluacionDesempeno
        fields = ['criterios', 'puntuacion', 'comentarios']
        widgets = {
            'criterios': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }