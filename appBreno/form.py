from django.forms import ModelForm
from django import forms
from .models import Tabela


class CadastroForm(ModelForm):
    class Meta:
        model = Tabela
        fields = ['nome', 'cpf', 'email', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class':'w3-input w3-border w3-text-blue'}),
            'cpf': forms.TextInput(attrs={'class': 'w3-input w3-border w3-text-blue'}),
            'email': forms.TextInput(attrs={'class': 'w3-input w3-border w3-text-blue'}),
            'telefone': forms.TextInput(attrs={'class': 'w3-input w3-border w3-text-blue'})
        }