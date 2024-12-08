from datetime import timezone
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import DocumentoForm
from django.core.mail import send_mail
from .models import Documento, Visualizacion
from django.utils import timezone
from django.utils.timezone import now


# Página principal
def index(request):
    return render(request, 'index.html')

# Función para generar el enlace
def generar_enlace(request, documento, correo_usuario):
    enlace = request.build_absolute_uri(
        reverse('correspondencia:seguimiento_documento', kwargs={'pk': documento.pk})
    )
    enlace_con_correo = f"{enlace}?correo={correo_usuario}"
    return enlace_con_correo

# Registrar un documento
def registrar_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save()

            # Obtener el correo del destinatario (suponiendo que está en el campo 'destinatario')
            correo_destinatario = documento.destinatario

            # Llamar a la función para generar el enlace
            enlace = generar_enlace(request, documento, correo_destinatario)
            
            mensaje_adicional = f'''
                Se ha registrado un nuevo documento con los siguientes detalles:
                Código: {documento.codigo}
                Fecha: {documento.fecha}
                Hora: {documento.hora}
                Referencia: {documento.referencia}
                Institución: {documento.institucion}
                Remitente: {documento.remitente}
                Observación: {documento.observacion}
                Fojas: {documento.fojas}
                Estado: {documento.estado}

                Puedes ver el documento aquí: {enlace}
                '''
                
            # Enviar correo electrónico al destinatario
            send_mail(
                subject='Nuevo documento registrado',
                message=mensaje_adicional,
                from_email='isatest172813@gmail.com',  # Cambia esto a tu correo real
                recipient_list=[documento.destinatario],
                fail_silently=False,
            )

            # Registrar la visualización (si el destinatario es el usuario que está viendo el documento)
            Visualizacion.objects.create(
                usuario=correo_destinatario,  # Correo del destinatario
                documento=documento,
                accion='No Visto',  # Inicialmente lo creamos como No Visto
            )

            # Redirigir a la vista de detalle pasando el documento.id
            return redirect('correspondencia:documento_detalle', pk=documento.pk)
    else:
        form = DocumentoForm()

    return render(request, 'registrar_documento.html', {'form': form})

# Detalle de un documento
def documento_detalle(request, pk):
    # Obtener el documento por su primary key (pk)
    documento = get_object_or_404(Documento, pk=pk)

    # Obtener las visualizaciones asociadas al documento
    visualizaciones = Visualizacion.objects.filter(documento=documento)

    # Renderizar la plantilla con los detalles del documento y las visualizaciones
    return render(request, 'documento_detalle.html', {
        'documento': documento,
        'visualizaciones': visualizaciones,
    })
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

    return render(request, 'documento_detalle.html', {'form': form, 'documento': documento})

# Eliminar un documento
def eliminar_documento(request, pk):
    # Obtener el documento por su PK desde la URL
    documento = get_object_or_404(Documento, pk=pk)
    documento.delete()  # Elimina el documento de la base de datos
    return redirect('correspondencia:lista_documentos')  # Redirige a la lista de documentos


def seguimiento_documento(request, pk):
    # Obtener el documento por su primary key (pk)
    documento = get_object_or_404(Documento, pk=pk)

    # Obtener el correo electrónico del usuario desde los parámetros GET
    correo_usuario = request.GET.get('correo')

    # Valor predeterminado para el estado de visualización
    estado_visualizacion = "No Visto"

    if correo_usuario:
        # Buscar si ya existe una visualización para este documento y usuario
        visualizacion = Visualizacion.objects.filter(
            documento=documento,
            usuario=correo_usuario
        ).first()  # Usamos `first()` para obtener la primera coincidencia si existe

        # Si no existe la visualización, se crea
        if not visualizacion:
            visualizacion = Visualizacion.objects.create(
                documento=documento,
                usuario=correo_usuario,
                fecha_visualizacion=now()  # Establecemos la fecha de visualización
            )
            estado_visualizacion = "Visto"  # Lo marcamos como "Visto" al crearlo

        # Si ya existe la visualización, se verifica si tiene fecha de visualización
        elif visualizacion.fecha_visualizacion:
            estado_visualizacion = "Visto"  # Si ya tiene fecha de visualización, es "Visto"
        else:
            # Si no tiene fecha, lo marcamos como "No Visto"
            estado_visualizacion = "No Visto"

    # Si no se pasó un correo (esto aplica a los administradores o vistas generales)
    else:
        # Verificar si el documento ha sido visualizado por alguien (admins)
        visualizaciones = Visualizacion.objects.filter(documento=documento)
        if visualizaciones.exists():
            estado_visualizacion = "Visto"
        else:
            estado_visualizacion = "No Visto"

    # Obtener todas las visualizaciones del documento
    visualizaciones = Visualizacion.objects.filter(documento=documento)

    # Pasar la información a la plantilla
    return render(request, 'seguimiento_documento.html', {
        'documento': documento,
        'visualizaciones': visualizaciones,
        'estado_visualizacion': estado_visualizacion,
    })
