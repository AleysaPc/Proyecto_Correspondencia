from django.urls import path
from . import views

app_name = 'correspondencia'

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.registrar_documento, name='registrar_documento'),
    path('lista/', views.lista_documentos, name='lista_documentos'),

    
]
