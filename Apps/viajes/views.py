from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.

def inicio(request):
    return render(request, 'viajes.html', {'viajes':Viaje.objects.all(),
                                          'titulo':'VIAJES'})

def administracion(request):
    if request.method == 'POST':
        try:
            form = ViajeForm(request.POST)
            if form.is_valid():
                viaje = form.save()
                bus = viaje.bus
                bus.horario.add(viaje.horario)
                total = int(request.POST.get('asientos',40))
                asientos_list = [
                    Asientos(bus=bus, horario=viaje.horario)
                    for _ in range(total)
                ]
                Asientos.objects.bulk_create(asientos_list)
                messages.success(request, 'Se guardó con éxito el Viaje y los asientos')
            else:
                messages.warning(request, 'Rellena los campos adecuadamente')
                return render(request, 'administracion_viajes.html', {'formulario':form,
                                                               'titulo':'Administración de VIAJES'})
        except Exception as e:
            messages.error(request, e)

        return redirect('/viajes/')
    else:
        return render(request, 'administracion_viajes.html', {'formulario':ViajeForm(),
                                                               'titulo':'Administración de VIAJES'})

def eliminar(request, id):
    if request.method == 'POST':
        try:
            Viaje.objects.get(id=id).delete()
            messages.success(request,'Se ha eliminado correctamente el viaje')
            return redirect('/viajes/')
        except Exception as e:
            messages.error(request, f'Hay un error: {e}')
            return redirect('/viajes/')
    else:
        return render(request, 'administracion_viajes.html', {'formulario':ViajeForm(),
                                                               'titulo':'Administración de VIAJES'})
    
def editar(request, id):
    viaje = Viaje.objects.get(id=id)
    form = ViajeForm(instance=viaje)
    if request.method == 'POST':
        try:
            form = ViajeForm(request.POST, instance = viaje)
            if form.is_valid():
                form.save()
                messages.success(request, 'Se editó con éxito el viaje')
            else:
                messages.warning(request, 'Rellena los campos adecuadamente')
        except Exception as e:
            messages.error(request, e)
            return render(request, 'administracion_viajes.html', {'formulario':form,
                                                               'titulo':'Administración de VIAJES'})
        return redirect('/viajes/')
    else:
        return render(request, 'administracion_viajes.html', {'formulario':form,
                                                       'titulo':'Administración de VIAJES'})

