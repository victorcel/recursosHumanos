from io import BytesIO
from django.http.response import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

width, height = A4


def generar_pdf(request):
 # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer,pagesize=A4)
    p.setLineWidth(.30)
    p.setFont('Helvetica',22)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(30, 750, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response