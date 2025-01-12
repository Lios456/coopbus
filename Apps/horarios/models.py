from django.db import models
from django import forms

# Create your models here.

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True)
    hora = models.TimeField()

    def __str__(self):
        return f"{self.codigo} {self.hora}"
    
class HorarioForm(forms.ModelForm):

    class Meta:

        model = Horario
        fields = '__all__'
        widgets={
            'codigo' : forms.TextInput(attrs={'class':'form-control'}),
            'hora' : forms.TimeInput(attrs={'class':'form-control', 'type':'time'})
        }

