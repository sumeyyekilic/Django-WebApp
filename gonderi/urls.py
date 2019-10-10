from django.conf.urls import url
from .views import *
#bu dosyayı kendimiz oluşturduk. bir uyg oluşturunca otomatik gelmez kendimiz olut. gerek.
from django.contrib import admin
app_name='gonderi'

urlpatterns = [
    url(r'^index/$', gonderi_index, name='index'),
    url(r'^create/$', gonderi_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', gonderi_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', gonderi_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', gonderi_delete, name='delete'),
]