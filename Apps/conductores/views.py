from django.shortcuts import render
from django.contrib import messages
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'conductores.html', {'conductores': Conductores.objects.all()})

def guardar(request):
    if request.method == 'POST':
        form = ConductoresForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Se guardó con éxito")
            except Exception as e:
                messages.error(request, f"Hubo un error: {e}")
        else:
            messages.error(request, "El formulario no está correctamente lleno")
    else:
        return render(request, 'administracion_conductores.html', {'form': ConductoresForm()})
