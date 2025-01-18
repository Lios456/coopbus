from django.shortcuts import render
from django.contrib.auth.decorators import *
# Create your views here.
@login_required(login_url='/usuarios/login')
def index(request):
    return render(request, 'index.html')