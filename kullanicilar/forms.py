#form kütüphanesi
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class GirisForm(forms.Form):
    kismi = forms.CharField(max_length=100, label='Kullanıcı Adı')
    ksifre = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
    #formun kontrolü
    def clean(self):
        kismi = self.cleaned_data.get('kismi')
        ksifre = self.cleaned_data.get('ksifre')
        if kismi and ksifre:
            kullanici = authenticate(username=kismi, password=ksifre)
            if not kullanici:
                raise forms.ValidationError("Kullanıcı adını veya şifreyi yanlış girdiniz!")
        return super(GirisForm, self).clean()

class KayitForm(forms.ModelForm):

    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password1 = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Parola Doğrulama', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        ksifre1 = self.cleaned_data.get("password1")
        ksifre2 = self.cleaned_data.get("password2")
        if ksifre1 and ksifre2 and ksifre1 != ksifre2:
            raise forms.ValidationError("Şifreler eşleşmiyor!")
        return ksifre2
