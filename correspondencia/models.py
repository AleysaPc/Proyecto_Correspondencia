from datetime import timezone
from django.db import models
from django.utils.timezone import now

class Documento(models.Model):
    
    codigo = models.CharField(max_length=5)
    fecha = models.DateField()
    hora = models.TimeField()
    referencia = models.CharField(max_length=255)
    institucion = models.CharField(max_length=100)
    remitente = models.CharField(max_length=30)
    cargoRemitente = models.CharField(max_length=30)
    observacion = models.CharField(max_length=255)
    fojas = models.IntegerField()
    estado = models.CharField(max_length=20)
    archivo = models.FileField(upload_to='documentos/')
    destinatario = models.EmailField()
   
    def __str__(self):
        return self.codigo
    
    def get_pdf_url(self):
        if self.archivo:
            return self.archivo.url
        return None
    
class Visualizacion(models.Model):
    usuario = models.CharField(max_length=100)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    accion = models.CharField(max_length=50)  # Este es el campo donde probablemente se presenta el error
    fecha_visualizacion = models.DateTimeField(auto_now_add=True)
