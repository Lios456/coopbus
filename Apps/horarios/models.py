from django.db import models
from django import forms
from ..rutas.models import Ruta

# Create your models here.

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True)
    hora = models.TimeField()
    ruta = models.ForeignKey(Ruta, related_name='ruta_del_horario', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.codigo} {self.hora}"
    
class HorarioForm(forms.ModelForm):

    class Meta:

        model = Horario
        fields = '__all__'
        widgets={
            'codigo' : forms.TextInput(attrs={'class':'form-control'}),
            'hora' : forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'ruta' : forms.Select(attrs={'class':'form-select'}),
        }

