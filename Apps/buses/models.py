from django.db import models
from django.forms import ModelForm
from django import forms
from ..conductores.models import Conductores
from ..rutas.models import Ruta
from ..horarios.models import Horario

class Buses(models.Model):
    id = models.AutoField(primary_key=True)

    placa = models.CharField(max_length=8, unique=True, verbose_name='PLACA')

    foto = models.ImageField(upload_to='buses/', default='bus.png', verbose_name='FOTO DE LA UNIDAD')

    conductor = models.ForeignKey(Conductores, on_delete=models.CASCADE, null=True, verbose_name='CONDUCTOR DE LA UNIDAD')

    marca = models.CharField(max_length=50, verbose_name='MARCA DE LA UNIDAD')

    anio = models.PositiveIntegerField(verbose_name='AÑO DE LA UNIDAD')

    ruta = models.ForeignKey(Ruta, on_delete=models.PROTECT, null=True, verbose_name='RUTA')

    horario = models.ManyToManyField(Horario, verbose_name='HORAIOS', null=True)

    estado = models.CharField(max_length=30, default='ACTIVO', verbose_name='ESTADO DE LA UNIDAD')

    asientos = models.PositiveIntegerField(default=40, verbose_name='¿CUÁNTOS ASIENTOS PARA PASAJEROS TIENE LA UNIDAD?')

    def __str__(self):
        return f'{self.placa} {self.conductor}'

class BusForm(ModelForm):
    class Meta:
        model = Buses
        fields = '__all__'
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'conductor': forms.Select(attrs={'class': 'form-select'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'asientos': forms.NumberInput(attrs={'class': 'form-control'}),
            'ruta': forms.Select(attrs={'class': 'form-select'}),
            'horario' :forms.Select(attrs={'class': 'form-select'}),
        }

class Asientos(models.Model):
    id = models.AutoField(primary_key=True)
    bus = models.ForeignKey(Buses, on_delete=models.CASCADE, related_name='puestos')
