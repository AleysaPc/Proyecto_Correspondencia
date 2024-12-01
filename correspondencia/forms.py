from django import forms
from .models import Documento

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['fecha', 'hora', 'referencia', 'institucion', 'remitente', 'cargoRemitente', 
                  'observacion', 'fojas', 'estado', 'archivo', 'destinatario']  # No incluimos 'codigo' porque es generado automáticamente

    # Personalizamos los widgets
    def __init__(self, *args, **kwargs):
        super(DocumentoForm, self).__init__(*args, **kwargs)
        
        # Si la instancia del formulario tiene un documento (es decir, estamos editando)
        if self.instance and self.instance.pk:
            # Hacer los campos no editables solo si estamos editando
            self.fields['fecha'].widget.attrs['readonly'] = 'readonly'
            self.fields['hora'].widget.attrs['readonly'] = 'readonly'
        else:
            # Si estamos creando un nuevo documento, no aplicamos readonly
            self.fields['fecha'].widget.attrs.pop('readonly', None)
            self.fields['hora'].widget.attrs.pop('readonly', None)

    fecha = forms.DateField(
        widget=forms.TextInput(attrs={
            'type': 'date',
        })
    )
    hora = forms.TimeField(
        widget=forms.TextInput(attrs={
            'type': 'time',
        })
    )
