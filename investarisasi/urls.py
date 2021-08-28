
from django.urls import path
from . import views
from djgeojson.views import GeoJSONLayerView
from .models import Investarisasi,Sawah,Kebun,SemakBelukar,Hutan,LahanKosong,Tambak,Sungai,Lainnya,Jalan,BatasDesa;

app_name='peta'

urlpatterns = [
    path('',views.peta,name='index'),
    path('dataSawah', GeoJSONLayerView.as_view(model=Sawah,properties=('luas', 'pemilik','jenis')), name='dataSawah'),
    path('dataKebun', GeoJSONLayerView.as_view(model=Kebun,properties=('luas', 'pemilik','jenis')), name='dataKebun'),
    path('dataHutan', GeoJSONLayerView.as_view(model=Hutan,properties=('luas', 'pemilik','jenis')), name='dataHutan'),
    path('dataLahanKosong', GeoJSONLayerView.as_view(model=LahanKosong,properties=('luas', 'pemilik','jenis')), name='dataLahanKosong'),
    path('dataTambak', GeoJSONLayerView.as_view(model=Tambak,properties=('luas', 'pemilik','jenis')), name='dataTambak'),
    path('dataSemakBelukar', GeoJSONLayerView.as_view(model=SemakBelukar,properties=('luas', 'pemilik','jenis')), name='dataSemakBelukar'),
    # path('dataBangunan', GeoJSONLayerView.as_view(model=Bangunan,properties=('luas', 'pemilik','jenis')), name='dataBangunan'),
    path('dataSungai', GeoJSONLayerView.as_view(model=Sungai,properties=('panjang','jenis')), name='dataSungai'),
    path('dataLainnya', GeoJSONLayerView.as_view(model=Lainnya,properties=('luas', 'pemilik','jenis')), name='dataLainnya'),
    path('dataJalan', GeoJSONLayerView.as_view(model=Jalan,properties=()), name='dataJalan'),
    path('dataBatas', GeoJSONLayerView.as_view(model=BatasDesa,properties=()), name='dataBatas'),
]
