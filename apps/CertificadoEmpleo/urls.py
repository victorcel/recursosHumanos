from django.conf.urls import url
from apps.CertificadoEmpleo.views import generar_pdf, prueba


app_name = 'certificado'

urlpatterns = [
    url(r'^prueba/$', prueba, name='prueba'),
    url(r'^empleado/$', generar_pdf, name='generar_pdf'),
]