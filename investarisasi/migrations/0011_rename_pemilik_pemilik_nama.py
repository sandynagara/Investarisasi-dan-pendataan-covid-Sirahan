# Generated by Django 3.2 on 2021-08-07 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investarisasi', '0010_investarisasi_pemilik'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pemilik',
            old_name='Pemilik',
            new_name='nama',
        ),
    ]