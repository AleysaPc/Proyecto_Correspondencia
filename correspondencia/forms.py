from django import forms
from .models import Documento

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['fecha', 'hora', 'referencia', 'institucion', 'remitente', 'cargoRemitente', 
                  'observacion', 'fojas', 'estado', 'archivo', 'destinatario']  # No incluimos 'codigo' porque es generado automáticamente

    # Opcional: personalizar los widgets si deseas un formato específico para algún campo
    fecha = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))
    