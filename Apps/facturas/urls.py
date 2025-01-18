from django.urls import path
from . import views
urlpatterns = [
   path('factura/<int:venta_id>/pdf/', views.generar_pdf,),

]
