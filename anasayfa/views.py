from django.shortcuts import render, HttpResponse

# Create your views here.
def anasayfa_view(request):
    if request.user.is_authenticated(): #kullanıcı giriş yaptıysa
        #göndermek istenen içerikler contexte
        context={
            'isim':'sümeyye',
        }
    else:

        context={
            'isim':'misafir'
        }        #göndermek istenen içerikler contexte
    return render(request,'anasayfa.html',context)


