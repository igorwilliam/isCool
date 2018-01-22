from django.db import models

# Create your models here.

class Discipline(models.Model):

    teacher = models.ForeignKey('accounts.User', verbose_name='Professor(a)', on_delete=models.DO_NOTHING)
    name = models.CharField('Nome', max_length=25)
    description = models.TextField('Descição')

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.name

class RegisterStudent(models.Model):
    STATUS_CHOICE = (
        (0, 'Aguardando Confirmação'),
        (1, 'Adicionado na Disciplina'),
        (2, 'Solicitação Recusada'),
    )

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        unique_together = (('student', 'discipline'),)
        ordering = ['-join']



    student = models.ForeignKey('accounts.User', verbose_name='Aluno', on_delete=models.DO_NOTHING)
    discipline = models.ForeignKey('Discipline', verbose_name='Disciplina', on_delete=models.DO_NOTHING)
    status = models.IntegerField('Situação', choices=STATUS_CHOICE, default=0)
    join = models.DateTimeField('Registrado', auto_now_add=True)
