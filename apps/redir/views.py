import re
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Redir
from usuario.models import User


def visualizar_redir(request, processo_id):
    if request.user.is_authenticated:    
        redir = get_object_or_404(Redir, pk=processo_id)

        redir_view = {
            'redir_view' : redir
        }

        return render(request, 'redir/visualizar-redir.html', redir_view)
    else:
        return redirect('usuario.login')


def criar_redir(request):
    if request.user.is_authenticated:

        etapas = 1
        if request.user.cargo == 'Gestor':
            etapas = 2
        if request.user.cargo == 'Diretor':
            etapas = 3
    
        if request.method == 'POST':
            gerencia = request.POST['gerencia']
            assunto = request.POST['Assunto']
            objecto = request.POST['objeto']
            empresa = request.POST['empresa']
            class_inf = request.POST['Classificacao_informacao']
            contex = request.POST['contextualizacao']
            valor_previsto = request.POST['Valor_previsto']
            valor_a_ser_pago = request.POST['Valor_para_ser_pago']
            rateado = request.POST['rateado']
            conclusao = request.POST['conclusao']
            apreciamento_interno = request.POST['apreciado_internamente']
            anexo_arquivo = request.FILES.get('anexar_arquivo')
            diretoria = request.POST['diretoria']
            fluxo = int(request.POST['fluxo'])
            if fluxo + etapas == 1:
                fluxo = 'Analista'
            elif fluxo + etapas == 2:
                fluxo = 'Gestor'
            elif fluxo + etapas == 3 and request.user.diretoria == 'DAF':
                fluxo = 'DAF'
            elif fluxo + etapas == 3 and request.user.diretoria == 'DO-DSG':
                fluxo = 'DO-DSG'
            elif fluxo + etapas == 3 and request.user.diretoria == 'DP':
                fluxo = 'DP'
            elif fluxo + etapas == 4:
                fluxo = 'GGE'

            if empresa == 'None' or class_inf == 'None' or rateado == 'None' or apreciamento_interno == 'None':
                messages.error(request, 'Todos os campos devem ser preenchidos ou conter alguma opção')
                return redirect('redir.cadastro')
            else:
                pass
            



            user = get_object_or_404(User, pk=request.user.id)

            redir = Redir.objects.create(gerencia=gerencia, usuario=user, empresa=empresa, class_inf=class_inf, assunto=assunto, objecto=objecto, contextualizacao=contex, valor_previsto=valor_previsto, 
            valor_a_ser_pago=valor_a_ser_pago, rateado=rateado, conclusao=conclusao, apreciamento_interno=apreciamento_interno, anexo_arquivo=anexo_arquivo, diretoria=diretoria, fluxo=fluxo)
            redir.save()
            messages.success(request, 'Redir Cadatrada com sucesso')
            return redirect('usuario.dashboard')
        return render(request, 'redir/cadastro-redir.html')
    else:
        return redirect('usuario.login')


def editar_redir(request, processo_id):
    if request.user.is_authenticated:
        redir = get_object_or_404(Redir, pk=processo_id)

        redir_editar = {
            'redir_editar': redir
        }
               
        return render(request, 'redir/editar-redir.html', redir_editar)
    else:
        return redirect('usuario.login')


def deletar_redir(request, processo_id):
    if request.user.is_authenticated:
        redir = get_object_or_404(Redir, pk=processo_id)
        redir.delete()
        return redirect('usuario.dashboard')
    else:
        return redirect('usuario.login')


def atualizar_redir(request):
    if request.user.is_authenticated:
        etapas = 1
        if request.user.cargo == 'Gestor':
            etapas = 2
        if request.user.cargo == 'Diretor':
            etapas = 3


        if request.method == 'POST':
            redir = request.POST['redir_id']
            r = Redir.objects.get(pk=redir)

            if r.usuario_id == request.user.id:
                r.area = request.POST.get('area')
                r.assunto = request.POST.get('Assunto')
                r.objecto = request.POST.get('objeto')
                r.empresa = request.POST.get('empresa')
                r.class_inf = request.POST.get('Classificacao_informacao')
                r.contextualizacao = request.POST.get('contextualizacao')
                r.valor_previsto = request.POST.get('Valor_previsto')
                r.valor_a_ser_pago = request.POST.get('Valor_para_ser_pago')
                r.rateado = request.POST.get('rateado')
                r.conclusao = request.POST.get('conclusao')
                r.apreciamento_interno = request.POST.get('apreciado_internamente')
            r.parecer_gge = request.POST.get('parecer_gge')
            r.aprovar = request.POST.get('aprovar')
            if request.FILES:
                r.anexo_arquivo = request.FILES.get('anexar_arquivo')
            if request.user.diretoria == 'DAF':
                r.parecer_daf = request.POST.get('parecer_daf')
            elif request.user.diretoria == 'DO-DSG':
                r.parecer_do = request.POST.get('parecer_do')
            elif request.user.diretoria == 'DP':
                r.parecer_dp = request.POST.get('parecer_dp')
                
                
            r.fluxo = int(request.POST['fluxo'])
            
            if r.fluxo == 2:
                r.fluxo = 'Concluir'
    
            elif r.fluxo + etapas == 1:
                r.fluxo = 'Analista'

            elif r.fluxo  + etapas == 2:
                r.fluxo = 'Gestor'
                
            elif r.fluxo + etapas == 3 and request.user.diretoria == 'DAF':
                r.fluxo = 'DAF'

            elif r.fluxo + etapas == 3 and request.user.diretoria == 'DO-DSG':
                r.fluxo = 'DO-DSG'

            elif r.fluxo + etapas == 3 and request.user.diretoria == 'DP':
                r.fluxo = 'DP'

            elif r.fluxo + etapas == 4:
                r.fluxo = 'REDIR'


            if r.aprovar == '' or r.fluxo == 0:
                messages.error(request, 'Todoas os campos devem conter alguma opção!, Tente novamente.')
                return redirect('usuario.dashboard')
                
                      
            
           

            r.save()
            messages.success(request, 'Redir Atualizada com sucesso') 
            return redirect('usuario.dashboard')
        else:
            return redirect('usuario.login')
    else:
        return redirect('usuario.login')