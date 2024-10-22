from django import forms
from .models import Gonderi, Yorum
#from captcha.fields import ReCaptchaField


#bu dosyaya gonderi modelimizi referans verdm
class GonderiForm(forms.ModelForm):
    #captcha = ReCaptchaField()

    class Meta:
        model=Gonderi
        fields={
            'baslik',
            'yazi',
            'image',
        }

class YorumForm(forms.ModelForm):
    #captcha = ReCaptchaField()

    def __init__(self,*args,**kwargs):
        super(YorumForm, self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}
        self.fields['yazi'].widget.attrs['row']=100
        self.fields['name'].widget.attrs['cols']=50
        self.fields['yazi'].widget.attrs['placeholder']='yorum yapınız...'
    class Meta:
        model=Yorum
        fields=[
            'name',
            'yazi'
        ]