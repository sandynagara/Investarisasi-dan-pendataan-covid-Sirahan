from django.db import models

# Create your models here.
from django.contrib.gis.db import models as gismodels

class Pemilik(models.Model):
    nama = models.CharField(max_length=80)

    def __str__(self):
        return self.nama

class Investarisasi(models.Model):
    jenis = gismodels.CharField(max_length=50)
    luas = gismodels.FloatField()
    pemilik = gismodels.CharField(max_length=50)
    note = gismodels.CharField(max_length=100)
    geom = gismodels.MultiPolygonField(srid=4326)

class JenisLahan(models.Model):
    jenis = models.CharField(max_length=80)

    def __str__(self):
        return self.jenis

class Sawah(models.Model):
    luas = gismodels.FloatField()
    pemilik = gismodels.ForeignKey(Pemilik,on_delete=models.CASCADE,null=True,blank=True,default="1")
    jenis = gismodels.ForeignKey(JenisLahan,on_delete=models.CASCADE,null=True,blank=True,default="1")
    geom = gismodels.MultiPolygonField(srid=4326)

class Kebun(models.Model):
    luas = gismodels.FloatField()
    pemilik = gismodels.ForeignKey(Pemilik,on_delete=models.CASCADE,null=True,blank=True,default="1")
    jenis = gismodels.ForeignKey(JenisLahan,on_delete=models.CASCADE,null=True,blank=True,default="2")
    geom = gismodels.MultiPolygonField(srid=4326)

class SemakBelukar(models.Model):
    luas = gismodels.FloatField()
    pemilik = gismodels.ForeignKey(Pemilik,on_delete=models.CASCADE,null=True,blank=True,default="1")
    jenis = gismodels.ForeignKey(JenisLahan,on_delete=models.CASCADE,null=True,blank=True,default="3")
    geom = gismodels.MultiPolygonField(srid=4326)

class Tambak(models.Model):
    luas = gismodels.FloatField()
    pemilik = gismodels.ForeignKey(Pemilik,on_delete=models.CASCADE,null=True,blank=True,default="1")
    jenis = gismodels.ForeignKey(JenisLahan,on_delete=models.CASCADE,null=True,blank=True,default="4")
    geom = gismodels.MultiPolygonField(srid=4326)

class LahanKosong(models.Model):
    luas = gismodels.FloatField()
    pemilik = gismodels.ForeignKey(Pemilik,on_delete=models.CASCADE,null=True,blank=True,default="1")
    jenis = gismodels.ForeignKey(JenisLahan,on_delete=models.CASCADE,null=True,blank=True,default="5")
    geom = gismodels.MultiPolygonField(srid=4326)

class Hutan(models.Model):
    luas = gismodels.FloatField()
    pemilik = gismodels.ForeignKey(Pemilik,on_delete=models.CASCADE,null=True,blank=True)
    jenis = gismodels.ForeignKey(JenisLahan,on_delete=models.CASCADE,null=True,blank=True,default="6")
    geom = gismodels.MultiPolygonField(srid=4326)

class Sungai(models.Model):
    panjang = gismodels.FloatField()
    jenis = gismodels.ForeignKey(JenisLahan,on_delete=models.CASCADE,null=True,blank=True,default="8")
    geom = gismodels.MultiPolygonField(srid=4326)

class Lainnya(models.Model):
    luas = gismodels.FloatField()
    pemilik = gismodels.ForeignKey(Pemilik,on_delete=models.CASCADE,null=True,blank=True)
    jenis = gismodels.ForeignKey(JenisLahan,on_delete=models.CASCADE,null=True,blank=True,default="9")
    geom = gismodels.MultiPolygonField(srid=4326)

class Jalan(models.Model):
    geom = gismodels.MultiPolygonField(srid=4326)

class BatasDesa(models.Model):
    geom = gismodels.LineStringField(srid=4326)