from django.forms import ModelForm
from .models import Tabela


class CadastroForm(ModelForm):
    class Meta:
        model = Tabela
        fields = ['nome', 'cpf', 'email', 'telefone']