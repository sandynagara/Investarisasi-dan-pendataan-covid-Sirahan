from django.urls import path
from . import views
from .models import DaftarCovid

app_name='peta'

urlpatterns = [
    path('',views.peta,name='index'),
    path('simpan',views.simpan,name='simpan'),
  
]