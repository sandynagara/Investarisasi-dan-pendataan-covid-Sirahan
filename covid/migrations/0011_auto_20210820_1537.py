# Generated by Django 3.2 on 2021-08-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0010_auto_20210820_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaftarCovid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('tempatLahir', models.CharField(max_length=255)),
                ('nomorHp', models.IntegerField()),
                ('tesCovid', models.BooleanField(default=False)),
                ('demam', models.BooleanField(default=False)),
                ('pilek', models.BooleanField(default=False)),
                ('bernafas', models.BooleanField(default=False)),
                ('tenggorokan', models.BooleanField(default=False)),
                ('lamaPenyakit', models.BooleanField(default=False)),
                ('kontak', models.BooleanField(default=False)),
                ('tinggal', models.BooleanField(default=False)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Pasien',
        ),
    ]