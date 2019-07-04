from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect,redirect
from .models import Gonderi
from .form import GonderiForm
from django.contrib import messages

def gonderi_index(request):
    gonderis=Gonderi.objects.all()
    #httpresponsu render metoduna çevircez.
    return render(request, 'gonderi/index.html',{ 'gonderis': gonderis })

def gonderi_detail(request,id):
    #gonderi=Gonderi.objects.get(id=1)
    #return  HttpResponse('BURASI post detail sayfası')
    gonderi=get_object_or_404(Gonderi, id=id)
    context={
        'gonderi':gonderi,
    }
    return render(request,'gonderi/detail.html',context)

def gonderi_create(request):

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
            gonderi = form.save()  # yönlendirme sayfası için geri dönen değeri gönderi adındaki değişkene atadım
            messages.success(request, 'Başarılı şekilde gonderi oluşturuldu')
            return HttpResponseRedirect(gonderi.get_absolute_url())
    else:
        # formu kullanıcıya göster (doldurulacak şekilde)

        form = GonderiForm()

    return render(request, "gonderi/form.html", context)

def gonderi_update(request,id):

    gonderi=get_object_or_404(Gonderi, id=id) #gonderiyi getirir
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

def gonderi_delete(request,id):
    #silmek istenen gönderi nesnesi gelsin
    gonderi=get_object_or_404(Gonderi, id=id)

    #getirilen nesne sil
    gonderi.delete()

    #gönderi silinirken detay sayfasında silincek.
    #yönlendirmeyi indexe yap, bunun için redirect metodunu  import et.
    #url.py de adresi düzenlemeyi unutma
    return redirect('gonderi:index')