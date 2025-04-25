from django import forms

# Formulario de loggeo
class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)