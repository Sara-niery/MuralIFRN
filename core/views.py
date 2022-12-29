from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario,Coordenacao,Aviso
from .forms import CoordenacaoForm,UsuarioForm,AvisoForm

def home(request):
    return render(request, 'index.html')

def recentes(request):
    return render(request, 'recentes.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')

def autenticar(request):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha'] 
        user = authenticate(request, username=usuario, password=senha)
        
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            return render (request, 'registration\login.html')

    else:    
        return render(request, 'registration\login.html')

def desconectar(request):
    logout(request)
    return redirect('home')

def registro(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto = {
        'form' : form
    }
    return render(request, 'registro.html', contexto)



def listar_usuario(request):
    usuarios = Usuario.objects.all()
    
    contexto = {
        'todos_usuarios' : usuarios
    }
    return render(request,'cruds/usuarios.html', contexto)

def cadastrar_usuario(request):
    form = UsuarioForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_usuario')

    contexto = {
       'form_usuario': form
    }
    return render(request,'cruds/usuario_cadastrar.html', contexto)

def atualizar_usuario(request, id):
    meus_usuarios = Usuario.objects.get(id=id)
    
    form = UsuarioForm(request.POST or None, request.FILES or None, instance = meus_usuarios)
    
    if form.is_valid():
         form.save()
         return redirect('listar_usuario')
   
    contexto = {
        "form_usuario": form
    }
    return render(request, 'cruds\\usuario_editar.html', contexto )      

def deletar_usuario(request, id):
    meus_usuarios = Usuario.objects.get(id=id)
    meus_usuarios.delete()
    return redirect('listar_usuario')



def listar_coordenacao(request):
    coord = Coordenacao.objects.all()
    
    contexto = {
        'todas_coord' : coord
    }
    return render(request,'cruds\\coordenacao.html', contexto)

def cadastrar_coordenacao(request):
    form = CoordenacaoForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_coordenacao')

    contexto = {
       'form_coordenacao': form
    }
    return render(request,'cruds\\coordenacao_cadastrar.html', contexto)

def atualizar_coordenacao(request, id):
    minhas_coordenacoes = Coordenacao.objects.get(id=id)
    
    form = CoordenacaoForm(request.POST or None, request.FILES or None, instance = minhas_coordenacoes)
    
    if form.is_valid():
         form.save()
         return redirect('listar_coordenacao')
   
    contexto = {
        "form_coordenacao": form
    }
    return render(request, 'cruds/coordenacao_editar.html', contexto )      

def deletar_coordenacao(request, id):
    minhas_coordenacoes = Coordenacao.objects.get(id=id)
    minhas_coordenacoes.delete()
    return redirect('listar_coordenacao')



def listar_avisos(request):
    avisos = Aviso.objects.all()
    context = {
        'todos_avisos' : avisos
    }
    return render(request,'cruds/avisos.html',context)

def cadastrar_avisos(request):
    form = AvisoForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        aviso = form.save(commit=False)
        aviso.usuario = request.user
        aviso.save()
        return redirect('listar_aviso')

    contexto = {
       'form_aviso': form
    }
    return render(request,'cruds/avisos_cadastrar.html', contexto)

def atualizar_aviso(request, id):
    meus_avisos = Aviso.objects.get(id=id)
    
    form = AvisoForm(request.POST or None, request.FILES or None, instance = meus_avisos)
    
    if form.is_valid():
         form.save()
         return redirect('listar_aviso')
   
    contexto = {
        "form_aviso": form
    }
    return render(request, 'cruds/aviso_editar.html', contexto )      

def deletar_aviso(request, id):
    meus_avisos = Aviso.objects.get(id=id)
    meus_avisos.delete()
    return redirect('listar_aviso')



