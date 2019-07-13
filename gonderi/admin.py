from django.contrib import admin

# Register your models here.
from .models import Gonderi
class gonderiAdmin(admin.ModelAdmin):
    list_display = ['baslik','yayin_tarihi','slug'] #admin sayfasında slugı incelemek için slug paramtresi eklendi
    #yayin tarihine tıklama ve detay görüntüleme içn
    list_display_links = ['yayin_tarihi']
    #filtreleme
    list_filter = ['yayin_tarihi']
    search_fields = ['baslik','yazi']
    #listelenen ekran üzerinde kayıt yenileme sağlayan:
    list_editable = ['baslik']

    class Meta:
        model=Gonderi

admin.site.register(Gonderi,gonderiAdmin)