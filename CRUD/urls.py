"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appBreno.views import cadastro,listagem, editar, excluir, home, login

urlpatterns = [
    path('', login, name='url_login'),
    path('home/', home, name='url_home'),
    path('admin/', admin.site.urls),
    path('cadastro/', cadastro, name='url_cadastro'),
    path('editar/<int:pk>/', editar, name='url_editar'),
    path('excluir/<int:pk>', excluir, name='url_excluir'),
    path('listagem/', listagem, name='url_listagem'),
]
