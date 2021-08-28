from django.shortcuts import render,redirect
from django.core import serializers
from django.core.serializers import serialize
from django.contrib import messages
from .models import Pemilik,JenisLahan;
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'isi.html')

def tambah(request):
    return render(request,'create.html')

def peta(request):
    pemilik = Pemilik.objects.all()
    jenisLahan = JenisLahan.objects.all()
    nama = serializers.serialize("json", pemilik)
    lahan = serializers.serialize("json", jenisLahan)
    context = {
        "nama":nama,
        "lahan":lahan
    } 
    return render(request,'peta.html',context)
