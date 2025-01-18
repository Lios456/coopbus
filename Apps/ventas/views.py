import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import *
from ..buses.models import *
from ..viajes.models import *
from django.db.models import *
from django.db.models.functions import *

# Create your views here.

def dash(request):
    context = {'titulo': 'Panel de Ventas',
               'ventas':Venta.objects.all(),
               'total_ventas':Venta.objects.select_related('horario__ruta').aggregate(total_ventas=Sum('horario__ruta__precio'))['total_ventas'],
               'ventas_por_anio':(
                        Venta.objects
                        .annotate(anio=ExtractYear('fecha'))
                        .values('anio')
                        .annotate(total_ventas=Sum('horario__ruta__precio'))
                        .order_by('anio')
                    ),
                'ventas_por_mes':(
                        Venta.objects
                        .annotate(mes=ExtractMonth('fecha'))
                        .values('mes')
                        .annotate(total_ventas=Sum('horario__ruta__precio'))
                        .order_by('mes')
                    )
               }
    return render(request, 'dash.html', context)

def venta(request):
    if request.method == 'POST':
        try:
            asientos_seleccionados = request.POST.getlist('puestos')
            if asientos_seleccionados:
                v = Venta()
                v.cliente = Cliente.objects.get(id = int(request.POST.get('cliente_id')))
                v.bus = Buses.objects.get(id = int(request.POST.get('id_bus')))
                v.horario = Viaje.objects.get(id = int(request.POST.get('id_viaje'))).horario
                v.save()
                
                for _ in asientos_seleccionados:
                    asi = Asientos.objects.get(id=_)
                    asi.ocupado = True
                    asi.save()
                    v.asiento.add(asi)
                messages.success(request, f'Asientos seleccionados: {asientos_seleccionados}')  
            else:
                messages.error(request, 'No hay asientos')
            return redirect('/ventas/')
        except Exception as e:
            messages.error(request, f'Error: {e}')
            return redirect('/ventas/')
    else:
        try:
            context = {
                    'titulo': 'Panel de Ventas',
                    'buses': Buses.objects.all()
                }
            dni = request.GET.get('cliente_dni')
            id_bus = request.GET.get('bus_id')
            id_viaje = request.GET.get('id_viaje')
            #Regreso el cliente
            if dni:
                cliente = Cliente.objects.get(dni=dni)
                context['cliente']= cliente
                
            #Regreso el bus y los viajes del bus

            if id_bus :
                context['bus'] = Buses.objects.get(id=id_bus)
                context['viajes'] = Viaje.objects.filter(bus = Buses.objects.get(id=id_bus))
            
            #Regreso el horario y los asientos

            if id_viaje:
                viaje = Viaje.objects.get(id = id_viaje)
                context['viaje'] = viaje
                context['asientos'] = Asientos.objects.filter(horario=viaje.horario)
                
        except Exception as e:
            messages.error(request, f'Error: {e}')

        return render(request, 'venta.html', context)
    
