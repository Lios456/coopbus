from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'conductores.html', {'conductores': Conductores.objects.all()})

def administracion(request):
    if request.method == 'POST':
        form = ConductoresForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Se guardó con éxito")
                redirect('/conductores/')
            except Exception as e:
                messages.error(request, f"Hubo un error: {e}")
                return render(request, 'administracion_conductores.html', {'form': form})
        else:
            messages.error(request, "El formulario no está correctamente lleno")
            return render(request, 'administracion_conductores.html', {'form': form})
    else:
        return render(request, 'administracion_conductores.html', {'form': ConductoresForm()})
    
def eliminar(request, id):
    if request.method == 'POST':
        try:
            Conductores.objects.get(id=id).delete()
            messages.success(request,'Se ha eliminado correctamente el Conductor')
            return redirect('/conductores/')
        except Exception as e:
            messages.error(f'Hay un error: {e}')
            return redirect('/conductores/')
    else:
        return render(request, 'conductores.html', {'conductores': Conductores.objects.all()})
    
def editar(request, id):
    conductor = Conductores.objects.get(id=id)
    form = ConductoresForm(instance=conductor)
    if request.method == 'POST':
        try:
            form = ConductoresForm(request.POST, request.FILES, instance = conductor)
            if form.is_valid():
                form.save()
                messages.success(request, 'Se guardó con éxito el Conductor')
            else:
                messages.warning(request, 'Rellena los campos adecuadamente')
        except Exception as e:
            messages.error(request, e)

        return redirect('/conductores/')
    else:
        return render(request, 'administracion_conductores.html', {'form': form})
