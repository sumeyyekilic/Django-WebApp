from django.db import models
from django.urls import reverse
# Create your models here.

class Gonderi(models.Model):
    baslik=models.CharField(max_length=120, verbose_name='başlık')
    yazi=models.TextField(verbose_name='içerik') #uzun yazılar yazma TextField
    yayin_tarihi=models.DateTimeField(verbose_name='yayınlanma tarihi', auto_now_add=True)
    image=models.ImageField(null=True, blank=True) #GONDERİ OLUŞTURULURKEN RESİM EKLEME
    #model yapısımnda değişiklik, vt ye aktar ( mikemigration , migrate)


    #TÜM GÖNERİLERİN BAŞLIĞININ aynı görünmesini kaldırır baslık nesnesini göstersin
    def __str__(self):
        return self.baslik

    def get_absolute_url(self):
        #return "/gonderi/{}".format(self.id)
        return reverse('gonderi:detail', kwargs={'id':self.id})

    #oluşturulan gönderinin yönetimi için silme, güncelleme,oluşturma
    # butonlarına ait fonsiyon yönlendirmeleri
    def get_create_url(self):
        return reverse('gonderi:create', kwargs={'id': self.id})
    def get_update_url(self):
        #return "/gonderi/{}".format(self.id)
        return reverse('gonderi:update', kwargs={'id':self.id})

    def get_delete_url(self):
        #return "/gonderi/{}".format(self.id)
        return reverse('gonderi:delete', kwargs={'id':self.id})

    class Meta:
        #son eklenen göneriyi en başa alma
        ordering=['-yayin_tarihi', 'id' ]