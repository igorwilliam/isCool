from django.db import models

# Create your models here.

class Topic(models.Model):

    title = models.CharField('Título', max_length=100)
    content = models.TextField('Conteúdo')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    discipline = models.ForeignKey('discipline.Discipline', verbose_name='Disciplina', on_delete=models.DO_NOTHING)
    is_warning = models.BooleanField('Aviso', default=False)
    author = models.ForeignKey('accounts.User', verbose_name='Autor', on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'
        ordering = ['-created']

    def __str__(self):
        return self.title

class Reply(models.Model):

    content = models.TextField('Comentário')
    topic = models.ForeignKey('post.Topic', verbose_name='Tópico', on_delete=models.DO_NOTHING)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    author = models.ForeignKey('accounts.User', verbose_name='Autor', on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.content
