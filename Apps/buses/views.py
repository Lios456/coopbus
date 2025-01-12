from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
# Create your views here.

def buses(request):
    return render(request, 'buses.html', {'total_buses':Buses.objects.count()})

def administracion(request):
    if request.method == 'POST':
        try:
            form = BusForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Se guardó con éxito el Bus')
            else:
                messages.warning(request, 'Rellena los campos adecuadamente')
        except Exception as e:
            messages.error(request, e)

        return redirect('/buses/administracion')
    else:
        return render(request, 'administracion.html', {'buses':Buses.objects.filter(estado='ACTIVO'),'formulario':BusForm()})

def guardar(request):
    if request.method == 'POST':
        messages.success(request, 'Se guardó con éxito el Bus')
        pass
    else:
        return render(request, 'administracion.html', {'buses':Buses.objects.filter(estado='ACTIVO'),'formulario':BusForm()})
    
def editar(request, id):
    bus = Buses.objects.get(id=id)
    form = BusForm(instance=bus)
    if request.method == 'POST':
        try:
            form = BusForm(request.POST, request.FILES, instance = bus)
            if form.is_valid():
                form.save()
                messages.success(request, 'Se guardó con éxito el Bus')
            else:
                messages.warning(request, 'Rellena los campos adecuadamente')
        except Exception as e:
            messages.error(request, e)

        return redirect('/buses/administracion')
    else:
        return render(request, 'administracion.html', {'buses':Buses.objects.filter(estado='ACTIVO'),'formulario':form})
