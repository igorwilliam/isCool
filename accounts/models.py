import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Apelido / Usuário', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de Usuário Válido. '
                'Este valor deve conter apenas letras e números.'
                'e os caracteres: @/./+/-/_.'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    name = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-mail')
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    is_student = models.BooleanField('Aluno', default=False)
    is_moderator = models.BooleanField('Moderador', default=False)
    is_teacher = models.BooleanField('Professor', default=False)

    avatar = models.ImageField('Avatar', upload_to='avatars', blank='true', default='avatars/user.png')


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        # permissions = (
        #     ('teacher', 'professor'),
        #     ('moderator', 'moderador'),
        #     ('student', 'aluno'),
        # )

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]
