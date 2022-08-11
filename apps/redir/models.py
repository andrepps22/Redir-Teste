from django.db import models
from datetime import datetime
from usuario.models import User


class Redir(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=100)
    class_inf = models.CharField(max_length=100)
    assunto = models.CharField(max_length=150)
    objecto = models.CharField(max_length=150)
    contextualizacao = models.TextField()
    valor_previsto = models.CharField(max_length=15)
    valor_a_ser_pago = models.CharField(max_length=15)
    rateado = models.CharField(max_length=10)
    conclusao = models.TextField()
    anexo_arquivo = models.FileField(upload_to='redir/%d-%m-%Y', blank=True)
    
    parecer_daf = models.TextField(blank=True, default='', null=True)
    parecer_do = models.TextField(blank=True, default='', null=True)
    parecer_dp = models.TextField(blank=True, default='', null=True)
    apreciamento_interno = models.TextField(blank=True)
    parecer_gge = models.TextField(blank=True, default='', null=True)
    aprovar = models.CharField(max_length=60, blank=True, default='', null=True)
    fluxo = models.CharField(max_length=60)
    data_publicacao = models.DateTimeField(default=datetime.now, blank=True)
    gerencia = models.CharField(max_length=100)
    diretoria = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.assunto
