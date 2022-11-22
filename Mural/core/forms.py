from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario,Coordenacao,Aviso
from django.forms import ModelForm

class AvisoForm(ModelForm):
    imagem = forms.FileField
    class Meta:
        model = Aviso
        fields = ['titulo','imagem','descricao','links']

class CoordenacaoForm(ModelForm):
    class Meta:
        model = Coordenacao
        fields = ['Coord']

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','password1','password2','email','nome','cargo']

