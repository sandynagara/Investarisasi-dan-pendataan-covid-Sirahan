# Generated by Django 3.2 on 2021-08-07 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investarisasi', '0002_auto_20210807_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investarisasi',
            name='pemilik',
            field=models.CharField(max_length=50),
        ),
    ]
