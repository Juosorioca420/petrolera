from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CreateUserForm( UserCreationForm ):
    '''
    Definir caracteristicas del {{ form }} para habilitar
    entradas de informacion a la hora del registro, editando 
    sobre el objeto UserCreationForm que se define por defecto en Django
    
        - username : nombre de usuario
        - email : correo del usuario
        - pswd1 : nueva contraseña
        - pswd2 : confirmacion de la contraseña

    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm( forms.ModelForm ):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm( forms.ModelForm ):
    class Meta:
        model = Profile
        fields = ['cc', 'image']

class AdminUpdateForm( forms.ModelForm ):
    class Meta:
        model = Profile
        fields = ['position']
