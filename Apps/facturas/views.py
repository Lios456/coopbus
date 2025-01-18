from ..ventas.models import *
from django.http import HttpResponse
from reportlab.lib.pagesizes import *
from reportlab.pdfgen import canvas


def generar_pdf(request, venta_id):
    venta = Venta.objects.get(id=venta_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{venta.id}.pdf"'

    # Crear el objeto canvas para generar el PDF
    p = canvas.Canvas(response, pagesize=A4)

    # Definir el contenido del PDF
    p.setFont("Helvetica", 12)
    p.drawString(50, 800, f"Factura: {venta.id}")
    p.drawString(50, 750, f"Cliente: {venta.cliente}")
    p.drawString(50, 725, f"Fecha: {venta.fecha.strftime('%d/%m/%Y')}")
    p.drawString(50, 700, f"Horario: {venta.horario}")
    p.drawString(50, 650, f"Asientos:")
    espacio = 620
    for asiento in venta.asiento.all():
        p.drawString(150, espacio, f'{asiento}')
        espacio-=30
    
    #Calcular el total
    total = venta.horario.ruta.precio * venta.asiento.count()

    p.drawString(200, espacio-10, f'Total: {total}')

    # Finalizar y generar el PDF
    p.showPage()
    p.save()

    return response
