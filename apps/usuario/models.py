from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user = self.model(
            username=username, password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):

        user = self.create_user(
            username, password=password,
            **extra_fields
            )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
        
    
class User(AbstractBaseUser, PermissionsMixin):
    Cargo = [('Analista', 'Analista'), ('Gestor', 'Gestor'), ('Diretor', 'Diretor')]
    Gerencia = [('GTI', 'GTI'), ('GFA', 'GFA'), ('NGP', 'NGP'), ('GGE', 'GGE'), ('ASC', 'ASC'), ('NAT', 'NAT'),
    ('GCM', 'GCM'), ('GSB', 'GSB'), ('GBP', 'GBP'), ('GRE', 'GRE'), ('GGE','GGE'), ('DAF', 'DAF'), ('DO-DSG','DO-DSG'), ('DP','DP')]
    Diretoria = [('DAF','DAF'), ('DO-DSG','DO-DSG'), ('DP','DP')]


    username = models.CharField(max_length=100, unique=True)
    nome_completo = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    cargo = models.CharField(max_length=100, choices=Cargo)
    gerencia = models.CharField(max_length=100, choices=Gerencia)
    diretoria = models.CharField(max_length=100 ,choices=Diretoria)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField("date joined", default=timezone.now)


    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.nome_completo
