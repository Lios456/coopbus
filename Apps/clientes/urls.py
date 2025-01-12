from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('administracion/', views.administracion),
    path('administracion/eliminar/<int:id>', views.eliminar),
    path('administracion/editar/<int:id>', views.editar),
]