from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class Gonderi(models.Model):
    # kullanıcıyı hangi model ile ilişkilendirmek istiyorsak foreignkey içine o model
    #related_name ise terminalden yapılan sorgulşarda gonderi_set yazmak yerine parametre sağlar
    kullanici=models.ForeignKey('auth.User', verbose_name='Yazar',related_name="gonderis")
    baslik=models.CharField(max_length=120, verbose_name='başlık')
    yazi=RichTextField(verbose_name='içerik') #uzun yazılar yazma TextField
    yayin_tarihi=models.DateTimeField(verbose_name='yayınlanma tarihi', auto_now_add=True)
    image=models.ImageField(null=True, blank=True) #GONDERİ OLUŞTURULURKEN RESİM EKLEME
    #model yapısında değişiklik, vt ye aktar ( mikemigration , migrate)
    #slug lanı artık id yerine başlık bilgisi gelmesi için tanımlı
    slug=models.SlugField(unique=True, editable=False, max_length=130)


    #TÜM GÖNERİLERİN BAŞLIĞININ aynı görünmesini kaldırır baslık nesnesini göstersin
    def __str__(self):
        return self.baslik

    def get_absolute_url(self):
        #return "/gonderi/{}".format(self.id)
        return reverse('gonderi:detail', kwargs={'slug':self.slug})

    #oluşturulan gönderinin yönetimi için silme, güncelleme,oluşturma
    # butonlarına ait fonsiyon yönlendirmeleri
    def get_create_url(self):
        return reverse('gonderi:create', kwargs={'slug': self.slug})
    def get_update_url(self):
        #return "/gonderi/{}".format(self.id)
        return reverse('gonderi:update', kwargs={'slug':self.slug})

    def get_delete_url(self):
        #return "/gonderi/{}".format(self.id)
        return reverse('gonderi:delete', kwargs={'slug':self.slug})

    def get_benzersiz_slug(self):
        slug = slugify(self.baslik.replace('ı', 'i'))
        benzersiz_slug = slug
        sayac = 1
        while Gonderi.objects.filter(slug=benzersiz_slug).exists():
            unique_slug = '{}-{}'.format(slug, sayac)
            sayac+= 1

        return benzersiz_slug

    def save(self, *args , **kwargs):
        self.slug=self.get_benzersiz_slug()
        return super(Gonderi,self).save(*args , **kwargs)

    class Meta:
        #son eklenen göneriyi en başa alma
        ordering=['-yayin_tarihi', 'id']

class Yorum(models.Model):
    gonderi=models.ForeignKey('gonderi.Gonderi',related_name='yorumlar', on_delete=models.CASCADE)
    name=models.CharField(max_length=200, verbose_name='isim')
    yazi=models.TextField(verbose_name='Yorum')
    yayin_tarihi=models.DateTimeField(auto_now_add=True)