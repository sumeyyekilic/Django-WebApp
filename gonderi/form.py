from django import forms
from .models import Gonderi, Yorum

#bu dosyaya gonderi modelimizi referans verdm
class GonderiForm(forms.ModelForm):
    class Meta:
        model=Gonderi
        fields={
            'baslik',
            'yazi',
            'image',
        }

class YorumForm(forms.ModelForm):
    class Meta:
        model=Yorum
        fields=[
            'name',
            'yazi'
        ]