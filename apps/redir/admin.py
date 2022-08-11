from django.contrib import admin
from .models import Redir

class ListRedir(admin.ModelAdmin):
    list_display = ('assunto', 'empresa', 'fluxo', 'aprovar', 'usuario', 'data_publicacao')

admin.site.register(Redir, ListRedir)
