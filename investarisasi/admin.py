from django.contrib import admin

# Register your models here.
from .models import Investarisasi,Pemilik,Sawah,Kebun,SemakBelukar,Hutan,LahanKosong,Tambak,Sungai,Lainnya,Jalan,BatasDesa,JenisLahan;
from leaflet.admin import LeafletGeoAdmin

class Admin(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_CENTER': (-7.760030, 110.376214), #atur zoom ke pogung
        'DEFAULT_ZOOM': 14,
    }
# daftarkan model pada halaman admin
admin.site.register(Sawah, Admin)
admin.site.register(Kebun, Admin)
admin.site.register(SemakBelukar, Admin)
admin.site.register(Hutan, Admin)
admin.site.register(LahanKosong, Admin)
admin.site.register(Tambak, Admin)
admin.site.register(Sungai, Admin)
admin.site.register(Lainnya, Admin)
admin.site.register(Jalan, Admin)
admin.site.register(JenisLahan)
admin.site.register(Pemilik)
