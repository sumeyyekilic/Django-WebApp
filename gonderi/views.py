from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect,redirect,Http404
from .models import Gonderi
from .form import GonderiForm,YorumForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def gonderi_index(request):
    gonderi_list=Gonderi.objects.all()
    query=request.GET.get('q')
    if query:
        gonderi_list=gonderi_list.filter(
            Q(baslik__icontains=query) |
            Q(yazi__icontains=query) |
            Q(kullanici__first_name__icontains=query) |
            Q(kullanici__last_name__icontains=query)
        ).distinct()
    paginator = Paginator(gonderi_list,6 )  # Show 25 contacts per page

    page = request.GET.get('Sayfa')
    try:
        gonderis= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        gonderis = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        gonderis = paginator.page(paginator.num_pages)

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