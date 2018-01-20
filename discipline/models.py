from django.db import models

# Create your models here.

class Discipline(models.Model):

    teacher = models.ForeignKey('accounts.User', verbose_name='Professor(a)', on_delete=models.DO_NOTHING)
    name = models.CharField('Nome', max_length=25)
    description = models.TextField('Descição')

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
