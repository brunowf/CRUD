from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tabela
from .form import CadastroForm


def login(request):
    return render(request,'appBreno/login.html')


def home(request):
    return render(request,'appBreno/home.html')


def cadastro(request):
    data={}
    form = CadastroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['cadastro'] = form
    return render(request, 'appBreno/cadastro.html', data)


def listagem(request):
    data={}
    data['lista'] = Tabela.objects.all()
    return render(request, 'appBreno/listagem.html', data)


def editar(request, pk):
    data={}

    tabela = Tabela.objects.get(pk=pk)
    form = CadastroForm(request.POST or None, instance=tabela)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['cadastro'] = form
    return render(request, 'appBreno/cadastro.html', data)


def excluir(request, pk):
    tabela = Tabela.objects.get(pk=pk)
    tabela.delete()
    return redirect('url_listagem')