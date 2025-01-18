from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group

class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        label="Grupo",
        help_text="Seleccione el grupo al que pertenece el usuario",
        widget=forms.Select(attrs={'class':'form-select'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='Ingesa el nombre del usuario'
    )
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='Ingesa la contraseña del usuario'
    )

    password2 = forms.CharField(
            widget=forms.TextInput(attrs={'class':'form-control'}),
            label='Vuelve a ingresar la contraseña del usuario'
        )


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'group']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        })
    )

    

