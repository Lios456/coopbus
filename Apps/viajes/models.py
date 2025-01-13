from django.db import models
from django import forms
from ..buses.models import *
from ..rutas.models import *

# Create your models here.

class Viaje(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=20, unique=True)
    ruta = models.ForeignKey(Ruta, verbose_name='RUTA', on_delete=models.DO_NOTHING)
    bus = models.ForeignKey(Buses, verbose_name='UNIDAD', on_delete=models.DO_NOTHING)
    horario = models.ForeignKey(Horario, verbose_name='HORARIO DEL VIAJE', on_delete=models.DO_NOTHING, related_name='horario_viaje')

    def __str__(self):
        return f'{self.codigo}'
    
class ViajeForm(forms.ModelForm):

    class Meta:

        model = Viaje
        fields = '__all__'
        widgets={
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'ruta': forms.Select(attrs={'class':'form-select'}),
            'bus': forms.Select(attrs={'class':'form-select'}),
            'horario': forms.Select(attrs={'class':'form-select'}),
        }

