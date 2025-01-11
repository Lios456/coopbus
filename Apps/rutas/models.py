from django.db import models

# Create your models here.

class Ruta(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True)
    partida = models.TextField(verbose_name='Lugar de Partida')
    destino = models.TextField(verbose_name='Lugar de Llegada')

    def __str__(self):
        return f'{self.codigo} [{self.partida} -- {self.destino}]'