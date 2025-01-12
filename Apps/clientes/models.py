from django.db import models
from django import forms

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(unique=True, max_length=10)
    apellido1 = models.CharField(max_length=150)
    apellido2 = models.CharField(max_length=150)
    nombres = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return f'{self.apellido1} {self.apellido2} {self.nombres}'
    
class ClienteForm(forms.ModelForm):

    class Meta:
        """Meta definition for Clienteform."""

        model = Cliente
        fields = '__all__'
        widgets ={
            'dni':forms.TextInput(attrs={'class':'form-control'}),
            'apellido1':forms.TextInput(attrs={'class':'form-control'}),
            'apellido2':forms.TextInput(attrs={'class':'form-control'}),
            'nombres':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

    
    
    
