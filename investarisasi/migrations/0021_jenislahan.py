# Generated by Django 3.2 on 2021-08-12 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investarisasi', '0020_auto_20210811_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='JenisLahan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=80)),
            ],
        ),
    ]
