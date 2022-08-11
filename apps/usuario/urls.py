from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='usuario.login'),
    path('dashboard/', views.dashboard, name='usuario.dashboard'),
    path('minhas_redirs/', views.minhas_redirs, name='usuario.minhas_redirs'),
    path('redirs_aprovar/', views.redirs_aprovadas, name='usuario.redirs_aprovadas'),
    path('logout/', views.logout, name='usuario.logout'),


] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
