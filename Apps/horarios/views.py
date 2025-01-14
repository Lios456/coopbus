from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.

def inicio(request):
    return render(request, 'horarios.html', {'horarios':Horario.objects.all(),
                                          'titulo':'HORARIOS'})

def administracion(request):
    if request.method == 'POST':
        try:
            form = HorarioForm(request.POST)
            if form.is_valid():
                form.save()
                
                messages.success(request, 'Se guardó con éxito el Horario')
            else:
                messages.warning(request, 'Rellena los campos adecuadamente')
                return render(request, 'administracion_horarios.html', {'formulario':form,
                                                               'titulo':'Administración de HORARIOS'})
        except Exception as e:
            messages.error(request, e)

        return redirect('/horarios/')
    else:
        return render(request, 'administracion_horarios.html', {'formulario':HorarioForm(),
                                                               'titulo':'Administración de HORARIOS'})

def eliminar(request, id):
    if request.method == 'POST':
        try:
            Horario.objects.get(id=id).delete()
            messages.success(request,'Se ha eliminado correctamente el horario')
            return redirect('/horarios/')
        except Exception as e:
            messages.error(request, f'Hay un error: {e}')
            return redirect('/horarios/')
    else:
        return render(request, 'administracion_horarios.html', {'formulario':HorarioForm(),
                                                               'titulo':'Administración de HORARIOS'})
    
def editar(request, id):
    horario = Horario.objects.get(id=id)
    form = HorarioForm(instance=horario)
    if request.method == 'POST':
        try:
            form = HorarioForm(request.POST, instance = horario)
            if form.is_valid():
                form.save()
                messages.success(request, 'Se editó con éxito el Horario')
            else:
                messages.warning(request, 'Rellena los campos adecuadamente')
        except Exception as e:
            messages.error(request, e)
            return render(request, 'administracion_horarios.html', {'formulario':form,
                                                               'titulo':'Administración de HORARIOS'})
        return redirect('/horarios/')
    else:
        return render(request, 'administracion_horarios.html', {'formulario':form,
                                                       'titulo':'Administración de HORARIOS'})

