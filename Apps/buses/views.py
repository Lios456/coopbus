from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
# Create your views here.

def buses(request):
    return render(request, 'buses.html', {'total_buses':Buses.objects.count(), 
                                          'buses':Buses.objects.all(),
                                          'titulo':'BUSES'})

def administracion(request):
    if request.method == 'POST':
        try:
            form = BusForm(request.POST)
            if form.is_valid():
                bus = form.save()

                total = int(request.POST.get('asientos',40))
                asientos_list = [
                    Asientos(bus=bus)
                    for _ in range(total)
                ]
                Asientos.objects.bulk_create(asientos_list)

                messages.success(request, 'Se guardó con éxito el Bus y generaron los asientos')
            else:
                messages.warning(request, 'Rellena los campos adecuadamente')
                return render(request, 'administracion.html', {'buses':Buses.objects.filter(estado='ACTIVO'),
                                                               'formulario':form,
                                                               'titulo':'Administración de BUSES'})
        except Exception as e:
            messages.error(request, e)

        return redirect('/buses/')
    else:
        return render(request, 'administracion.html', {'buses':Buses.objects.filter(estado='ACTIVO'),
                                                       'formulario':BusForm(),
                                                       'titulo':'Administración de BUSES'})

def eliminar(request, id):
    if request.method == 'POST':
        try:
            Buses.objects.get(id=id).delete()
            messages.success(request,'Se ha eliminado correctamente el bus')
            return redirect('/buses/')
        except Exception as e:
            messages.error(request, f'Hay un error: {e}')
            return redirect('/buses/')
    else:
        return render(request, 'administracion.html', {'buses':Buses.objects.filter(estado='ACTIVO'),
                                                       'formulario':BusForm(),
                                                       'titulo':'Administración de BUSES'})
    
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

        return redirect('/buses/')
    else:
        return render(request, 'administracion.html', {'buses':Buses.objects.filter(estado='ACTIVO'),
                                                       'formulario':form,
                                                       'titulo':'Administración de BUSES'})
