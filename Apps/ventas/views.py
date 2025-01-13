import json
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from .models import *
from ..buses.models import *

# Create your views here.

def dash(request):
    return render(request, 'dash.html', {'titulo': 'Panel de Ventas'})

def venta(request):
    if request.method == 'POST':
        try:
            asientos_seleccionados = request.POST.get('asientos')
        
            if asientos_seleccionados:
                asientos = json.loads(asientos_seleccionados)
                for _ in asientos:
                    asi = Asientos.objects.get(id=_)
                    asi.ocupado = True
                    asi.save()

                messages.success(request, f'Asientos seleccionados: {asi}')  # Muestra los asientos seleccionados
                # Aquí puedes procesar la lista de asientos seleccionados y hacer lo que necesites con ella
                # Ejemplo: realizar la reserva, guardar en la base de datos, etc.
            else:
                messages.error(request, 'No hay asientos')

            return JsonResponse({'status': 'success', 'asientos': asientos})
        except Exception as e:
            messages.error(request, f'Error: {e}')
    return render(request, 'venta.html', {'titulo': 'Panel de Ventas', 'form': VentaForm()})

def ver_horarios(request):
    try:
        idbus = request.GET.get('id_bus')
        bus = Buses.objects.get(id=idbus)
        horarios = list(bus.horario.all().values('id','hora'))
        return JsonResponse({'horarios': horarios})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    

def ver_asientos(request):
    try:
        idbus = request.GET.get('id_bus')
        idhorario = request.GET.get('id_horario')
        bus = Buses.objects.get(id=idbus)
        horario = Horario.objects.get(id=idhorario)
        asientos = list(Asientos.objects.filter(bus=bus, horario=horario).values('id','ocupado'))
        return JsonResponse({'asientos': asientos})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    


def ver_cliente(request):
    dni = request.GET.get('dni')
    try:
        cliente = Cliente.objects.get(dni=dni)
        data = {
            'id': cliente.id,
            'nombre_completo': f'{cliente.apellido1} {cliente.apellido2} {cliente.nombres}',
            'email': cliente.email
        }
        return JsonResponse(data)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado.'})
