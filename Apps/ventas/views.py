from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from .models import *
from ..buses.models import *

# Create your views here.

def dash(request):
    return render(request, 'dash.html', {'titulo': 'Panel de Ventas'})

def venta(request):
    return render(request, 'venta.html', {'titulo': 'Panel de Ventas', 'form': VentaForm()})

def ver_horarios(request):
    try:
        idbus = request.GET.get('id_bus')
        bus = Buses.objects.get(id=idbus)
        horarios = list(bus.horario.all().values_list('hora', flat=True))
        asientos = list(Asientos.objects.filter(bus=bus, ocupado=0).values('id', 'numero'))
        return JsonResponse({'horarios': horarios, 'asientos': asientos})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    

def ver_asientos(request):
    try:
        idbus = request.GET.get('id_bus')
        bus = Buses.objects.get(id=idbus)
        asientos = Asientos.objects.filter(bus=bus, ocupado=0)
    except Exception as e:
        return JsonResponse({'error': str(e)})
    


def ver_cliente(request):
    dni = request.GET.get('dni')
    try:
        cliente = Cliente.objects.get(dni=dni)
        data = {
            'nombre_completo': f'{cliente.apellido1} {cliente.apellido2} {cliente.nombres}',
            'email': cliente.email
        }
        return JsonResponse(data)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado.'})
