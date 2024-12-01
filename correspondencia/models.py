from datetime import timezone
from django.db import models

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
