# Generated by Django 3.2 on 2021-08-17 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pasien',
            name='Demam',
        ),
        migrations.RemoveField(
            model_name='pasien',
            name='Nama',
        ),
        migrations.RemoveField(
            model_name='pasien',
            name='NomorHandphone',
        ),
        migrations.RemoveField(
            model_name='pasien',
            name='RiwayatKontak',
        ),
        migrations.RemoveField(
            model_name='pasien',
            name='RiwayatMobilisasi',
        ),
        migrations.RemoveField(
            model_name='pasien',
            name='TanggalLahir',
        ),
        migrations.RemoveField(
            model_name='pasien',
            name='TesCovid',
        ),
    ]
