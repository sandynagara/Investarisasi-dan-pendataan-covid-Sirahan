# Generated by Django 3.2 on 2021-08-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investarisasi', '0006_investarisasi_pemilik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investarisasi',
            name='pemilik',
            field=models.CharField(max_length=50),
        ),
    ]