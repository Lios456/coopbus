from django.db import models
from django import forms
from ..conductores.models import Conductores
from ..rutas.models import Ruta
from ..horarios.models import Horario

class Buses(models.Model):
    id = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=8, unique=True, verbose_name='PLACA')
    foto = models.ImageField(upload_to='buses/', default='buses/bus.png', verbose_name='FOTO DE LA UNIDAD')
    conductor = models.ForeignKey(Conductores, on_delete=models.CASCADE, null=True, verbose_name='CONDUCTOR DE LA UNIDAD')
    marca = models.CharField(max_length=50, verbose_name='MARCA DE LA UNIDAD')
    anio = models.PositiveIntegerField(verbose_name='AÑO DE LA UNIDAD')
    horario = models.ManyToManyField(Horario, verbose_name='HORARIOS', null=True)
    estado = models.CharField(max_length=30, default='ACTIVO', verbose_name='ESTADO DE LA UNIDAD', choices=[('ACTIVO','ACTIVO'),('NO ACTIVO','NO ACTIVO')])

    def __str__(self):
        return f'{self.placa} {self.conductor}'

class BusForm(forms.ModelForm):
    class Meta:
        model = Buses
        fields = ['placa','foto','conductor','marca','anio','estado']
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'conductor': forms.Select(attrs={'class': 'form-select select2'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

class Asientos(models.Model):
    id = models.AutoField(primary_key=True)
    bus = models.ForeignKey(Buses, on_delete=models.CASCADE, related_name='puestos')
    horario = models.ForeignKey(Horario, related_name='horario_asiento', on_delete=models.RESTRICT, default='1')
    ocupado = models.BooleanField(verbose_name='ASIENTO', default=False)

    def __str__(self):
        return f'Asiento {self.id}'
