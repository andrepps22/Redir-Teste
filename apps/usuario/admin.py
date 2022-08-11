from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User

class ListUser(UserAdmin):
    list_filter = ('username', 'cargo', 'gerencia', 'is_active')
    list_display = ('username','cargo', 'gerencia', 'diretoria', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': ('nome_completo', 'email', 'cargo', 'gerencia', 'diretoria')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )

admin.site.register(User, ListUser)