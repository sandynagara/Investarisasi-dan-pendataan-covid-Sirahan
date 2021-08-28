import os
from django.contrib.gis.utils import LayerMapping
from .models import BatasDesa, Jalan, Lainnya,Sungai; # definisi gismodel dari `models.py`
# ==== bagian ini diperoleh dari ogrinspect ====
biasa = {
    'luas':'luas',
    'geom': 'MULTIPOLYGON',
}

sungai = {
    'panjang':'panjang',
    'geom': 'MULTIPOLYGON',
}

garis = {
    'geom': 'LineString25D',
}

luas = {
    'geom': 'MULTIPOLYGON',
}


# ============================================
#kebun_shp = os.path.abspath(
 #   os.path.join(os.path.dirname(__file__), 'data', 'kebun.shp'),
#)

Lainnya_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Lainnya.shp'),
)

Sungai_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Sungai.shp'),
)

Bangunan_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Bangunan.shp'),
)

Jalan_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Jalan.shp'),
)

BatasDesa_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'BatasDesa.shp'),
)



def run(verbose=True):
    lmSungai = LayerMapping(Sungai, Sungai_shp, sungai,transform=False)
#     lmBangunan = LayerMapping(Bangunan,Bangunan_shp, biasa,transform=False)
    lmLainnya = LayerMapping(Lainnya, Lainnya_shp, biasa,transform=False)
    lmJalan = LayerMapping(Jalan,Jalan_shp, luas,transform=False)
#    # lmKebun.save(strict=True, verbose=verbose)
    lmSungai.save(strict=True, verbose=verbose)
#     lmBangunan.save(strict=True, verbose=verbose)
    lmLainnya.save(strict=True, verbose=verbose)
    lmJalan.save(strict=True, verbose=verbose)



