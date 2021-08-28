from django.db import models

from django.contrib.gis.db import models as gismodels
# Create your models here.
class DaftarCovid(models.Model):
    nama = models.CharField(max_length=255)
    usia = models.IntegerField()
    nomorHp = models.BigIntegerField()
    tesCovid = models.BooleanField(default=False)
    demam = models.BooleanField(default=False)
    pilek = models.BooleanField(default=False)
    bernafas = models.BooleanField(default=False)
    tenggorokan = models.BooleanField(default=False)
    lamaPenyakit = models.BooleanField(default=False)
    kontak = models.BooleanField(default=False)
    tinggal = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=10,decimal_places=6)
    longitude = models.DecimalField(max_digits=10,decimal_places=6)
 
    def __str__(self):
        nama = self.nama
        return nama