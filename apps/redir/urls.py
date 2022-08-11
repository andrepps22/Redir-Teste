from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cadastro/', views.criar_redir, name='redir.cadastro'),
    path('editar/<int:processo_id>', views.editar_redir, name='redir.editar'),
    path('atualizar/', views.atualizar_redir, name='redir.atualizar'),
    path('visualizar/<int:processo_id>', views.visualizar_redir, name='redir.visualizar'),
    path('deletar/<int:processo_id>', views.deletar_redir, name='redir.deletar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)