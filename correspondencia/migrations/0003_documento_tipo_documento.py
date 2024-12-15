# Generated by Django 4.2.16 on 2024-12-15 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correspondencia', '0002_visualizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='tipo_documento',
            field=models.CharField(choices=[('enviado', 'Enviado'), ('recibido', 'Recibido')], default='recibido', max_length=10),
        ),
    ]
