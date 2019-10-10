from django.shortcuts import render, redirect
from .forms import KayitForm, GirisForm
from django.contrib.auth import authenticate, login, logout

def giris_view(request):
    form = GirisForm(request.POST or None)
    if form.is_valid():
        kismi = form.cleaned_data.get('kismi')
        ksifre = form.cleaned_data.get('ksifre')
        kullanici = authenticate(username=kismi, password=ksifre)
        login(request, kullanici)

        return redirect('anasayfa')

    return render(request, "kullanicilar/form.html", {'form': form, 'title': 'Giriş yap'})


def kayit_view(request):
    form = KayitForm(request.POST or None)
    if form.is_valid():
        kullanici = form.save(commit=False)
        sifre = form.cleaned_data.get('password1')
        kullanici.set_password(sifre)
        # user.is_staff = user.is_superuser = True
        kullanici.save()
        yeni_kullanici = authenticate(username=kullanici.username, password=sifre)
        login(request, yeni_kullanici)
        return redirect('anasayfa')

    return render(request, "kullanicilar/form.html", {"form": form, 'title': 'Kayıt Ol'})

def cikis_view(request):
    logout(request)
    return redirect('anasayfa')