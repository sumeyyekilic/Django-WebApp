from django import forms
from .models import Gonderi

#bu dosyaya gonderi modelimizi referans verdm
class GonderiForm(forms.ModelForm):
    class Meta:
        model=Gonderi
        fields={
            'baslik',
            'yazi',
        }