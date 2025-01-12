from django.urls import path
from . import views

urlpatterns = [

    path('', views.buses),
    path('administracion/', views.administracion),
    path('administracion/editar/<int:id>', views.editar),
    path('administracion/eliminar/<int:id>', views.eliminar),
]