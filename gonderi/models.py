from django.db import models
from  django.urls import reverse
# Create your models here.

class Gonderi(models.Model):
    baslik=models.CharField(max_length=120, verbose_name='başlık')
    yazi=models.TextField(verbose_name='içerik') #uzun yazılar yazma TextField
    yayin_tarihi=models.DateTimeField(verbose_name='yayınlanma tarihi', auto_now_add=True)

    #TÜM GÖNERİLERİN BAŞLIĞININ aynı görünmesini kaldırır baslık nesnesini göstersin
    def __str__(self):
        return self.baslik

    def get_absolute_url(self):
        #return "/gonderi/{}".format(self.id)
        return reverse('gonderi:detail', kwargs={'id':self.id})