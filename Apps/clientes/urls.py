from django.urls import path
from . import views

urlpatterns = [
    path('administracion/', views.administracion)
]