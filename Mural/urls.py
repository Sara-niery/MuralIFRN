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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import home, recentes
from core.views import cadastrar_usuario, atualizar_usuario, listar_usuario, deletar_usuario
from core.views import listar_aviso, cadastrar_aviso, atualizar_aviso, deletar_aviso
from core.views import autenticar,desconectar, perfil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('recentes/',recentes,name= 'recente'),
    path('perfil/', perfil, name='perfil'),
    path('login/', autenticar,name='login'),
    path('logout/', desconectar,name='logout'),

    path('usuario',listar_usuario, name='listar_usuario'),
    path('cadastrar_usuario/',cadastrar_usuario,name='cadastrar_usuario'),
    path('atualizar_usuario/<int:id>',atualizar_usuario,name='atualizar_usuario'),
    path('deletar_usuario/<int:id>', deletar_usuario,name='deletar_usuario'),

    path('aviso/',listar_aviso,name='listar_aviso'),
    path('cadastrar_aviso/',cadastrar_aviso,name='cadastrar_aviso'),
    path('atualizar_aviso/<int:id>',atualizar_aviso,name='atualizar_aviso'),
    path('deletar_aviso/<int:id>',deletar_aviso,name='deletar_aviso'),
    
]   +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)