
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('investarisasi/',include('investarisasi.urls', namespace='investarisasi')),
    path('covid/',include('covid.urls', namespace='covid')),
]
