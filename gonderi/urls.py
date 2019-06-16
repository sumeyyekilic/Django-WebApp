from django.conf.urls import url
from .views import *
#bu dosyayı kendimiz oluşturduk. bir uyg oluşturunca otomatik gelmez kendimiz olut. gerek.

app_name='gonderi'

urlpatterns = [
    url(r'^index/$', gonderi_index, name='index'),
    url(r'^(?P<id>\d+)/$', gonderi_detail, name='detail'),
    url(r'^create/$', gonderi_create, name='create  '),
    url(r'^(?P<id>\d+)/update/$', gonderi_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', gonderi_delete, name='delete'),
]