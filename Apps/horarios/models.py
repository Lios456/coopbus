from django.db import models

# Create your models here.

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True)
    hora = models.TimeField()

    def __str__(self):
        return f"{self.codigo} {self.hora}"
