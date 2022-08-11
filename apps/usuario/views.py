from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import auth, messages
from .models import User
from redir.models import Redir


def login(request):
    if request.method == 'POST':
        chave = request.POST['chave'].strip().upper()
        senha = request.POST['senha']
        if chave == '' or senha == '':
            messages.error(request, 'Preencha Todos os Campos')
            return redirect('usuario.login')

        user = auth.authenticate(request, username=chave, password=senha)
        if user is not None:
            auth.login(request, user)
            return redirect('usuario.dashboard')
    return render(request, 'usuario/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        try:
            redirs = get_list_or_404(Redir)
        except:
            pass

        gerencia = request.user.gerencia
        redir = Redir.objects.filter(gerencia=gerencia).exclude(fluxo__icontains='concluido')
        if request.user.cargo == 'Diretor':
            diretoria = request.user.diretoria
            redir = Redir.objects.filter(fluxo=diretoria)

        try:   
            for r in redirs:
                if r.fluxo == 'REDIR' and request.user.gerencia == 'GGE':
                    redir = Redir.objects.all
        except:
            pass

        dados = {
            'redir': redir
        }

        return render(request, 'usuario/dashboard.html', dados)
    else:
        messages.error(request, 'Necessario fazer login para acessar a pagina')
        return redirect('usuario.login')


def minhas_redirs(request):
    if request.user.is_authenticated:
        id = request.user.id
        redir = Redir.objects.filter(usuario=id)

        dados = {
            'redir': redir
        }

        return render(request, 'usuario/minhas_redir.html', dados)
    else:
        messages.error(request, 'Necessario fazer login para acessar a pagina')
        return redirect('usuario.login')


def redirs_aprovadas(request):
    if request.user.is_authenticated:
        diretoria = request.user.diretoria    
        
        
        redir = Redir.objects.filter(diretoria=diretoria)

        dados = {
            'redir': redir
        }

        return render(request, 'usuario/redirs_aprovadas.html', dados)
    else:
        messages.error(request, 'Necessario fazer login para acessar a pagina')
        return redirect('usuario.login')


def logout(request):
    auth.logout(request)
    return redirect('usuario.login')
