from .models import Pais, Estado
from django import forms


class formPais(forms.ModelForm):
    class Meta:
        model=Pais
        fields=['codigo','description']
        
class formEstado(forms.ModelForm):
    class Meta:
        model=Estado
        fields=['codigo','description']