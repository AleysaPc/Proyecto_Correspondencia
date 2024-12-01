from django.db import models

class Documento(models.Model):
    titulo = models.CharField(max_length=200)  # Título del documento
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional
    archivo = models.FileField(upload_to='documentos/')  # Archivo que se sube
    destinatario = models.EmailField()  # Dirección de correo del destinatario
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        return self.titulo
