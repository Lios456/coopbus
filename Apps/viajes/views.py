from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def inicio(request):
    return render(request, 'viajes.html', {'viajes':Viaje.objects.all(),
                                          'titulo':'VIAJES'})
@staff_member_required(login_url='/usuarios/login/')
def administracion(request):
    if request.method == 'POST':
        try:
            form = ViajeForm(request.POST)
            if form.is_valid():
                viaje = form.save()
                #Obtengo el bus
                bus = viaje.bus
                #Al bus obtenido del formulario le doy el horario y la ruta del viaje
                bus.horario.add(viaje.horario)
                bus.save()

                #Genero los asientos para ese viaje
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
@staff_member_required(login_url='/usuarios/login/')
def eliminar(request, id):
    if request.method == 'POST':
        try:
            viaje = Viaje.objects.get(id=id)
            #Elimino el horario y la ruta
            viaje.bus.horario.remove(viaje.horario)
            viaje.bus.save()
            #Elimino los asientos que sean de ese bus en ese horario
            asientos = Asientos.objects.filter(bus=viaje.bus, horario=viaje.horario)
            asientos.delete()
            viaje.delete()
            messages.success(request,'Se ha eliminado correctamente el viaje')
            return redirect('/viajes/')
        except Exception as e:
            messages.error(request, f'Hay un error: {e}')
            return redirect('/viajes/')
    else:
        return render(request, 'administracion_viajes.html', {'formulario':ViajeForm(),
                                                               'titulo':'Administración de VIAJES'})
@staff_member_required(login_url='/usuarios/login/') 
def editar(request, id):
    viaje = Viaje.objects.get(id=id)
    form = ViajeForm(instance=viaje)
    if request.method == 'POST':
        try:
            form = ViajeForm(request.POST, instance = viaje)
            if form.is_valid():
                viaje_ant = Viaje.objects.get(codigo = request.POST.get('codigo'))
                bus = viaje_ant.bus
                #quito el horario anterior
                bus.horario.remove(viaje_ant.horario)
                #obtengo los asientos con el horario anterior
                asientos = Asientos.objects.filter(bus=bus, horario=viaje_ant.horario)

                #actualizo los horarios
                viaje = form.save()
                bus.horario.add(viaje.horario)
                bus.save()
                asientos.update(horario = viaje.horario)
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

