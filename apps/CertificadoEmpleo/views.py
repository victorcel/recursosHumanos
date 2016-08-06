from io import BytesIO
from os import startfile
from django.contrib import messages


from django.http.response import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from apps.CertificadoEmpleo.forms import DatosForm
from apps.CertificadoEmpleo.models import Empleado


width, height = A4


def prueba(request):
    form = DatosForm(request.POST or None)
    message = ''
    resultado =''
    if request.method == 'POST':
        if form.is_valid():
            message = form.cleaned_data['cedula']
            try:
                resultado=Empleado.objects.get(cedula=message)
                if 'cedula' in request.POST:
                    return generar_pdf(request, '{} {}'.format(resultado.nombre,resultado.apellido))
            except Empleado.DoesNotExist:
                resultado='No existe'





    context = {'message': message,'resultado':resultado,'form': form }
    return render(request, 'prueba.html', context)


def generar_pdf(request, message):
    # message = ''
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setLineWidth(.30)
    p.setFont('Helvetica', 22)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(30, 750, "Hello world. " + message)
    p.drawImage('static/nao.png',440,720,100,100)

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    #startfile(pdf)
    response.write(pdf)

    # context = {'message' : message}
    #render(request , 'prueba.html',context)
    return response