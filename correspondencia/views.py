from django.shortcuts import get_object_or_404, render, redirect
from .forms import DocumentoForm
from django.core.mail import send_mail
from .models import Documento

# Página principal
def index(request):
    return render(request, 'index.html')

# Registrar un documento
def registrar_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save()

            mensaje_adicional = f'''
                Se ha registrado un nuevo documento con los siguientes detalles:
                Código: {documento.codigo}
                Fecha: {documento.fecha}
                Hora: {documento.hora}
                Referencia: {documento.referencia}
                Institución: {documento.institucion}
                Remitente: {documento.remitente}
                Observación: {documento.observacion}
                fojas: {documento.fojas}
                estado:{documento.estado}
                '''
                
            # Enviar correo electrónico al destinatario
            send_mail(
                subject='Nuevo documento registrado',
                message=mensaje_adicional,
                from_email='isatest172813@gmail.com',  # Cambia esto a tu correo real
                recipient_list=[documento.destinatario],
                fail_silently=False,
            )

            # Redirigir a la vista de detalle pasando el documento.id
            return redirect('correspondencia:documento_detalle', pk=documento.id)
    else:
        form = DocumentoForm()

    return render(request, 'registrar_documento.html', {'form': form})

# Detalle de un documento
def documento_detalle(request, pk):
    # Obtener el documento por su PK desde la URL
    documento = get_object_or_404(Documento, pk=pk)
    return render(request, 'documento_detalle.html', {'documento': documento})

# Lista de documentos
def lista_documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'lista_documentos.html', {'documentos': documentos})



# Editar un documento
def editar_documento(request, pk):
    # Obtener el documento por su PK desde la URL
    documento = get_object_or_404(Documento, pk=pk)

    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES, instance=documento)
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('correspondencia:lista_documentos')  # Redirige a la lista de documentos
    else:
        form = DocumentoForm(instance=documento)

    return render(request, 'editar_documento.html', {'form': form, 'documento': documento})

# Eliminar un documento
def eliminar_documento(request, pk):
    # Obtener el documento por su PK desde la URL
    documento = get_object_or_404(Documento, pk=pk)
    documento.delete()  # Elimina el documento de la base de datos
    return redirect('correspondencia:lista_documentos')  # Redirige a la lista de documentos
