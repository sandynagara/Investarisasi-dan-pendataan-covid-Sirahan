from django.contrib import admin

# Register your models here.
from leaflet.admin import LeafletGeoAdmin
from .models import DaftarCovid;

class Admin(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_CENTER': (-7.760030, 110.376214), 
        #atur zoom ke pogung
        'DEFAULT_ZOOM': 14,
    }

admin.site.register(DaftarCovid, Admin)