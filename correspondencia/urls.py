from django.conf import settings
from django.urls import path
from . import views


app_name = 'correspondencia'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('registrar/', views.registrar_documento, name='registrar_documento'),
    path('detalle/<int:pk>/', views.documento_detalle, name='documento_detalle'),
    path('lista/', views.lista_documentos, name='lista_documentos'),
    path('editar/<int:pk>/', views.editar_documento, name='editar_documento'),  # Para editar un documento
    path('eliminar/<int:pk>/', views.eliminar_documento, name=  'eliminar_documento'),  # Para eliminar un documento
    path('documento/seguimiento/<int:pk>/', views.seguimiento_documento, name='seguimiento_documento'),
    
    
]