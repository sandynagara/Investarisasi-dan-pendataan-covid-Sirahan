from django.shortcuts import render,redirect
from leaflet.forms.widgets import LeafletWidget
from django.contrib.gis.db import models as geo_models
from .models import DaftarCovid
from investarisasi.models import Pemilik
from django.core import serializers
from django.http import HttpResponse
 
# fom leaflet.forms.fields import PolygonField;
# # Create your views here.

# class Posisi(forms.Form):
#     posisi = forms.PointField()

def peta(request):
    daftarCovid = DaftarCovid.objects.all()
    pemilik = Pemilik.objects.all()
    daftar = serializers.serialize("json", daftarCovid)
    pemilik2 = serializers.serialize("json", pemilik)
    print(daftar)
    print(daftarCovid)
    context = {
         "nama":daftar,
        "pemilik":pemilik2,
    }

    return render(request,'petaCovid.html',context)

def ubah(kondisi):
    if kondisi=="true":
        return True
    else:
        return False

def simpan(request):
    daftar = DaftarCovid()
    daftar.nama = request.POST.get('nama')
    daftar.usia= request.POST.get('usia')
    daftar.nomorHp=request.POST.get('nomorHp')
    daftar.tesCovid = request.POST.get('tesCovid')
    print(request.POST,"2")

    daftar.demam= ubah(request.POST.get('Demam'))
    print(daftar.demam)
    daftar.pilek=ubah(request.POST.get('Pilek'))
    daftar.bernafas = ubah(request.POST.get('bernafas'))
    daftar.tenggorokan= ubah(request.POST.get('tenggorokan'))
    daftar.lamaPenyakit=ubah(request.POST.get('Lama'))
    daftar.kontak = ubah(request.POST.get('kontak'))
    daftar.tinggal = ubah(request.POST.get('tinggal'))
    daftar.latitude=request.POST.get('lat')
    daftar.longitude=request.POST.get('long')

    daftar.save()

    return redirect('/covid')

