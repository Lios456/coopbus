from django.urls import path
from . import views

urlpatterns = [

    path('', views.dash),
    path('nueva/', views.venta),
    path('ver_horarios/', views.ver_horarios),
    path('ver_asientos/', views.ver_asientos),
    path('ver_cliente/', views.ver_cliente),
        
]