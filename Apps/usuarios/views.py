from django.contrib.auth import login, logout, authenticate
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *


@staff_member_required(login_url='/usuarios/login/')
def inicio(request):
    context = {
        'usuarios': User.objects.all()
    }
    return render(request, 'users.html', context)

def register_view(request):
    if request.method == 'POST':
        try:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False) 
                user.save()
                group = form.cleaned_data['group']
                user.groups.add(group)  
                username = form.cleaned_data['username']
                raw_password = form.cleaned_data['password1']
                user = authenticate(username=username, password=raw_password)
                
                if user is not None:
                    login(request, user)
                    messages.success(request, "Registro exitoso. Ahora estás autenticado.")
                    return redirect('/')
                else:
                    messages.error(request, "Ocurrió un error al autenticar el usuario.")
            else:
                messages.error(request, "Por favor corrige los errores.")
        except Exception as e:
            messages.error(request, f"Error: {e}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect('/')
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('login')
