from django.shortcuts import render, redirect
from .forms import DocumentoForm
from django.core.mail import send_mail
from .models import Documento


def index(request):
    return render(request, 'index.html')

def registrar_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save()

            # Enviar correo electrónico al destinatario
            send_mail(
                subject='Nuevo documento registrado',
                message=f'Se ha registrado un nuevo documento: {documento.codigo}',
                from_email='isatest172813@gmail.com',  # Cambia esto
                recipient_list=[documento.destinatario],
                fail_silently=False,
            )

            return redirect('correspondencia:lista_documentos')
    else:
        form = DocumentoForm()

    return render(request, 'registrar_documento.html', {'form': form})


def lista_documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'lista_documentos.html', {'documentos': documentos})

