from django.db import models
from django import forms
from ..buses.models import *
from..rutas.models import *
from ..horarios.models import *
from ..clientes.models import *
# Create your models here.

class Venta(models.Model):
    id = models.BigAutoField(primary_key=1)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT, verbose_name='Para qué cliente es el asiento?')
    bus = models.ForeignKey(Buses, on_delete=models.RESTRICT, verbose_name='Unidad')
    horario = models.ForeignKey(Horario, on_delete=models.RESTRICT, verbose_name='Horario')
    asiento = models.ManyToManyField(Asientos, related_name='asientos')
    fecha = models.DateTimeField(auto_now=True)


class VentaForm(forms.ModelForm):

    class Meta:

        model = Venta
        fields = '__all__'
        widgets={
            'cliente' : forms.TextInput(attrs={'class':'form-select'}),
            'bus' : forms.Select(attrs={'class':'form-select'}),
            'horario' : forms.Select(attrs={'class':'form-select'}),
            'asiento' : forms.SelectMultiple(attrs={'class':'form-select'}),
        }


