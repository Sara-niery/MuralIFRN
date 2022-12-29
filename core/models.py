from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField('Nome', max_length= 100)
    cargo = models.CharField('cargo', max_length=50)
    
    class Meta:
        permissions = [
            ('gerenciar_mural', 'Permissão para cadastrar, editar, listar e remover avisos no mural'),
            ('admin', 'Adicionar descrição')
        ]

class Aviso(models.Model):
    titulo = models.CharField('Nome', max_length=50)
    imagem = models.ImageField('imagem', upload_to='imagens/',null=True)
    descricao = models.CharField('descrição', max_length=1000)
    links = models.CharField('links',max_length=500)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

#Tirar
class Coordenacao(models.Model):
    Coord = models.CharField('Nome', max_length=50)

