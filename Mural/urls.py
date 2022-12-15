"""Mural URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from core.views import home, recentes
from core.views import cadastrar_usuario, atualizar_usuario, listar_usuario, deletar_usuario
from core.views import listar_avisos, cadastrar_avisos, atualizar_aviso, deletar_aviso
from core.views import listar_coordenacao, cadastrar_coordenacao, atualizar_coordenacao, deletar_coordenacao
from core.views import autenticar,desconectar, registro, perfil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',home, name='home'),
    path('recentes/',recentes,name= 'recente'),
    path('perfil/', perfil, name='perfil'),
    path('login/', autenticar,name='login'),
    path('logout/', desconectar,name='logout'),
    path('registro/', registro, name='registro'),

    path('usuario',listar_usuario, name='listar_usuario'),
    path('cadastrar_usuario/',cadastrar_usuario,name='cadastrar_usuario'),
    path('atualizar_usuario/',atualizar_usuario,name='atualizar_usuario'),
    path('deletar_usuario', deletar_usuario,name='deletar_usuario'),

    path('aviso/',listar_avisos,name='listar_aviso'),
    path('cadastrar_avisos/',cadastrar_avisos,name='cadastrar_avisos'),
    path('atualizar_usuario/',atualizar_aviso,name='atualizar_aviso'),
    path('deletar_aviso/',deletar_aviso,name='deletar_aviso'),

    path('coord',listar_coordenacao,name='listar_coord'),
    path('cadastrar_coord',cadastrar_coordenacao ,name='cadastrar_coord'),
    path('atualizar_coord',atualizar_coordenacao,name='atualizar_coord'),
    path('deletar_coord',deletar_coordenacao, name='deletar_coord'),
]
