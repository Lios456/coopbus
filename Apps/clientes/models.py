from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(unique=True, max_length=10)
    apellido1 = models.CharField(max_length=150)
    apellido2 = models.CharField(max_length=150)
    nombres = models.CharField(max_length=150)
    email = models.EmailField()
    
    
    
