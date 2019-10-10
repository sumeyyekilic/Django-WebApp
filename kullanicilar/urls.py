from django.conf.urls import url
from .views import *

app_name='kullanicilar'

urlpatterns = [
    url(r'^giris/$', giris_view, name="giris"),

    url(r'^kayit/$', kayit_view, name="kayit"),
    url(r'^cikis/$', cikis_view, name="cikis"),
]