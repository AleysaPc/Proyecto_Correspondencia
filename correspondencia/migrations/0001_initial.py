# Generated by Django 4.2.16 on 2024-12-01 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('referencia', models.CharField(max_length=255)),
                ('institucion', models.CharField(max_length=100)),
                ('remitente', models.CharField(max_length=30)),
                ('cargoRemitente', models.CharField(max_length=30)),
                ('observacion', models.CharField(max_length=255)),
                ('fojas', models.IntegerField()),
                ('estado', models.CharField(max_length=20)),
                ('archivo', models.FileField(upload_to='documentos/')),
                ('destinatario', models.EmailField(max_length=254)),
            ],
        ),
    ]
