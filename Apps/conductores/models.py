from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

class Conductores(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(unique=True, max_length=10)
    foto = models.ImageField(upload_to='conductores/', default='conductores/conductor_default.png')
    apellido1 = models.CharField(max_length=150)
    apellido2 = models.CharField(max_length=150)
    nombres = models.CharField(max_length=150)
    email = models.EmailField()
    celular = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.dni} {self.apellido1} {self.apellido2} {self.nombres}"

class ConductoresForm(ModelForm):

    class Meta:

        model = Conductores
        fields = '__all__'
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'apellido1': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido2': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),

        }

