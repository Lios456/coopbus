from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'clientes.html', {'clientes': Cliente.objects.all(),
                                             'titulo':'Clientes'})

def administracion(request):
    if request.method == 'POST':
        try:
            form = ClienteForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f'El cliente con el DNI {request.POST.get('dni')} se ha guardado correctamente')
                return redirect('/clientes/')
            else:
                messages.error(request, 'El formulario no es correcto')
                return render(request, 'administracion_clientes.html', {'form': form})
        except Exception as e:
            messages.success(request,f'ERROR: {e}')
            return redirect('/clientes/administracion/')

    else:
        return render(request, 'administracion_clientes.html', {'form': ClienteForm()})
    
def editar(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'El cliente ha sido modificado correctamente')
            return redirect('/clientes/')
        else:
            messages.error(request, 'El formulario no está llenado correctamente')
            return render(request, 'administracion_clientes.html', {'form': form})
            
    else:
        return render(request, 'administracion_clientes.html', {'form': ClienteForm(instance=cliente)})


def eliminar(request):
    if request.method == 'POST':
        try:
            Cliente.objects.get(id=id).delete()
        except Exception as e:
            messages.success(request,'Se ha eliminado correctamente el bus')
            return redirect('/clientes/administracion/')
    else:
        return render(request, 'administracion_clientes.html', {'form': ClienteForm()})
