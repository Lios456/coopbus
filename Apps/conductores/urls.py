from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio ),
    path('agregar/', views.guardar ),
]