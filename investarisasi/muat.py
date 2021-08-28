import os
from django.contrib.gis.utils import LayerMapping
from .models import Kebun,Sawah,LahanKosong,SemakBelukar,Hutan,Tambak # definisi gismodel dari `models.py`
# ==== bagian ini diperoleh dari ogrinspect ====
kebun_sawah_mapping = {
    'pemilik': 'Pemilik',
    'luas':'luas',
    'geom': 'MULTIPOLYGON',
}
# ============================================
#kebun_shp = os.path.abspath(
 #   os.path.join(os.path.dirname(__file__), 'data', 'kebun.shp'),
#)

Sawah_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Sawah.shp'),
)

Kebun_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Kebun.shp'),
)

LahanKosong_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'LahanKosong.shp'),
)

SemakBelukar_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'SemakBelukar.shp'),
)

Hutan_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Hutan.shp'),
)

Tambak_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Tambak.shp'),
)

def run(verbose=True):
    lmSemakBelukar = LayerMapping(SemakBelukar, SemakBelukar_shp, kebun_sawah_mapping,transform=False)
    lmLahanKosong = LayerMapping(LahanKosong,LahanKosong_shp, kebun_sawah_mapping,transform=False)
    lmHutan = LayerMapping(Hutan, Hutan_shp, kebun_sawah_mapping,transform=False)
    lmTambak = LayerMapping(Tambak,Tambak_shp, kebun_sawah_mapping,transform=False)
    lmSawah = LayerMapping(Sawah, Sawah_shp, kebun_sawah_mapping,transform=False)
    lmKebun = LayerMapping(Kebun,Kebun_shp, kebun_sawah_mapping,transform=False)
   # lmKebun.save(strict=True, verbose=verbose)
    lmSemakBelukar.save(strict=True, verbose=verbose)
    lmLahanKosong.save(strict=True, verbose=verbose)
    lmHutan.save(strict=True, verbose=verbose)
    lmTambak.save(strict=True, verbose=verbose)
    lmSawah.save(strict=True, verbose=verbose)
    lmKebun.save(strict=True, verbose=verbose)



