# Generated by Django 3.2 on 2021-08-07 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investarisasi', '0005_remove_investarisasi_pemilik'),
    ]

    operations = [
        migrations.AddField(
            model_name='investarisasi',
            name='pemilik',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='investarisasi.pemilik'),
        ),
    ]
