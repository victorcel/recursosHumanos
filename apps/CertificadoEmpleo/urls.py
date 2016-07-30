from django.conf.urls import url
from apps.CertificadoEmpleo.views import generar_pdf


app_name = 'certificado'

urlpatterns = [
    url(r'^empleado/$', generar_pdf, name='generar_pdf'),
]