from django.db import models


class Tabela(models.Model):
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome, self.cpf


class TabelaSenha(models.Model):
    senha = models.CharField(max_length=50, null=True,blank=True)
    perguntinha = models.TextField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)