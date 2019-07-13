from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect,redirect,Http404
from .models import Gonderi
from .form import GonderiForm,YorumForm
from django.contrib import messages
from django.utils.text import slugify

def gonderi_index(request):
    gonderis=Gonderi.objects.all()
    #httpresponsu render metoduna çevircez.
    return render(request, 'gonderi/index.html',{ 'gonderis': gonderis })

def gonderi_detail(request,slug):
    #gonderi=Gonderi.objects.get(slug=slug)
    #return  HttpResponse('BURASI post detail sayfası')
    gonderi=get_object_or_404(Gonderi, slug=slug)

    if request.method == "POST":
        # GELEN BİLGİLERİ KAYDETSİN
        form = YorumForm(request.POST or None)  # request gonderiform değişkenini POST nesnesi haline getirir.
        if form.is_valid():
            yorum = form.save(
                commit=False)  # yönlendirme sayfası için geri dönen değeri gönderi adındaki değişkene atadım
            # save içerisindeki commit false alanı; nesneyi kaydetmeden çnce zorunlu alanıbelirlemeye izin versin
            yorum.gonderi = gonderi
            "    "  # istek yapan kullanıcıyı yazar yaptım
            yorum.save()  # nesne kaydı okeyle
            messages.success(request, 'Yorumunuz Başarılı Şekilde İletildi!')
            return HttpResponseRedirect(gonderi.get_absolute_url())
    else:
        # formu kullanıcıya göster (doldurulacak şekilde)

        form = YorumForm()
        context = {
            'gonderi': gonderi,
            'form': form,
        }
    return render(request,'gonderi/detail.html',context)

def gonderi_create(request):

    if not request.user.is_authenticated():
        #HTTP404 İMPORT
        return  Http404()
    form=GonderiForm()
    # form nesnesi üretildi
    context = {
        'form': form,
    }

    if request.method == "POST":
        # GELEN BİLGİLERİ KAYDETSİN
        form = GonderiForm(request.POST or None,
                           request.FILES or None)  # request gonderiform değişkenini POST nesnesi haline getirir.
        if form.is_valid():
            gonderi = form.save(commit=False)  # yönlendirme sayfası için geri dönen değeri gönderi adındaki değişkene atadım
            #save içerisindeki commit false alanı; nesneyi kaydetmeden çnce zorunlu alanıbelirlemeye izin versin
            gonderi.kullanici=request.user #istek yapan kullanıcıyı yazar yaptım
            gonderi.save() #nesne kaydı okeyle
            messages.success(request, 'Başarılı şekilde gonderi oluşturuldu')
            return HttpResponseRedirect(gonderi.get_absolute_url())
    else:
        # formu kullanıcıya göster (doldurulacak şekilde)

        form = GonderiForm()

    return render(request, "gonderi/form.html", context)

def gonderi_update(request,slug):
    if not request.user.is_authenticated():
        #HTTP404 İMPORT
        return  Http404()
    gonderi=get_object_or_404(Gonderi, slug=slug) #gonderiyi getirir
    form=GonderiForm(request.POST or None, request.FILES or None, instance=gonderi)
    # yukarda form getirme ve bu formugetirdiğinde gönderi bilgileri ile doldurmak için sondaki parametreye gonderi eklenir

    #kulanıcının yaptığı değiş. kaydet
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı şekilde gonderi oluşturuldu')
        return HttpResponseRedirect(gonderi.get_absolute_url())
    #form nesnesini içerik olarak gönder
    context = {
        'form' : form
    }
    return render(request, 'gonderi/form.html', context)

def gonderi_delete(request,slug):
    if not request.user.is_authenticated():
        #HTTP404 İMPORT
        return  Http404()
    #silmek istenen gönderi nesnesi gelsin
    gonderi=get_object_or_404(Gonderi, slug=slug)

    #getirilen nesne sil
    gonderi.delete()

    #gönderi silinirken detay sayfasında silincek.
    #yönlendirmeyi indexe yap, bunun için redirect metodunu  import et.
    #url.py de adresi düzenlemeyi unutma
    return redirect('gonderi:index')