from django.db import models
from django import forms

# Create your models here.

class Ruta(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True)
    partida = models.TextField(verbose_name='Lugar de Partida')
    destino = models.TextField(verbose_name='Lugar de Llegada')
    precio = models.DecimalField(verbose_name='Precio', default=0.3, max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.partida} - {self.destino}'
    
    
class RutaForm(forms.ModelForm):

    class Meta:

        model = Ruta
        fields = '__all__'
        widgets={
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'partida': forms.Textarea(attrs={'class':'form-control'}),
            'destino': forms.Textarea(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control', 'step':0.1, 'type':'number'})
        }
