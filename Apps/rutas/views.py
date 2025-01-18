from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def inicio(request):
    return render(request, 'rutas.html', {'rutas':Ruta.objects.all(),
                                          'titulo':'RUTAS'})
@staff_member_required(login_url='/usuarios/login/')
def administracion(request):
    if request.method == 'POST':
        try:
            form = RutaForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Se guardó con éxito la Ruta')
            else:
                messages.warning(request, 'Rellena los campos adecuadamente')
                return render(request, 'administracion_rutas.html', {'formulario':form,
                                                               'titulo':'Administración de RUTAS'})
        except Exception as e:
            messages.error(request, e)

        return redirect('/rutas/')
    else:
        return render(request, 'administracion_rutas.html', {'formulario':RutaForm(),
                                                               'titulo':'Administración de RUTAS'})
@staff_member_required(login_url='/usuarios/login/')
def eliminar(request, id):
    if request.method == 'POST':
        try:
            Ruta.objects.get(id=id).delete()
            messages.success(request,'Se ha eliminado correctamente la ruta')
            return redirect('/rutas/')
        except Exception as e:
            messages.error(request, f'Hay un error: {e}')
            return redirect('/rutas/')
    else:
        return render(request, 'administracion_rutas.html', {'formulario':RutaForm(),
                                                               'titulo':'Administración de RUTAS'})
@staff_member_required(login_url='/usuarios/login/')  
def editar(request, id):
    ruta = Ruta.objects.get(id=id)
    form = RutaForm(instance=ruta)
    if request.method == 'POST':
        try:
            form = RutaForm(request.POST, instance = ruta)
            if form.is_valid():
                form.save()
                messages.success(request, 'Se editó con éxito la ruta')
            else:
                messages.warning(request, 'Rellena los campos adecuadamente')
        except Exception as e:
            messages.error(request, e)
            return render(request, 'administracion_rutas.html', {'formulario':form,
                                                               'titulo':'Administración de RUTAS'})
        return redirect('/rutas/')
    else:
        return render(request, 'administracion_rutas.html', {'formulario':form,
                                                       'titulo':'Administración de RUTAS'})

