from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario,Coordenacao,Aviso
from .forms import CoordenacaoForm,UsuarioForm,AvisoForm

def home(request):
    return render(request, 'index.html')

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

#def listar_usuario(request):
    #usuarios = Usuario.objects.all()
    #contexto = {
     #   'todos_usuarios' : usuarios
    #}
    #return render(request,'cruds\usuarios.html',contexto)

#def cadastrar_usuario(request):
 #   form = UsuarioForm(request.POST or None,request.FILES or None)
  #  if form.is_valid():
   #     form.save()
    #    return redirect('listar_usuario')

    #contexto = {
     #   'form_usuario': form
    #}
    #return render(request,'cruds\usuario_cadastrar.html', contexto)

#def atualizar_usuario(request, id):
  #  meus_usuarios = Usuario.objects.get(id=id)
    
   # form = UsuarioForm(request.POST or None, request.FILES or None, instance = meus_usuarios)
    
   # if form.is_valid():
      #  form.save()
     #   return redirect('listar_usuario')
   
    #contexto = {
    #    "form_usuario": form
   # }
  #  return render(request, 'cruds\usuario_editar.html', contexto )      

def deletar_musica(request, id):
    meus_usuarios = Usuario.objects.get(id=id)
    meus_usuarios.delete()
    return redirect('listar_usuario')

def listar_coord(request):
    coord = Coordenacao.objects.all()
    context = {
        'todas_coord' : coord
    }
    return render(request,'cruds\coordenacao.html',context)

def listar_avisos(request):
    avisos = Aviso.objects.all()
    context = {
        'todos_avisos' : avisos
    }
    return render(request,'cruds\avisos.html',context)
