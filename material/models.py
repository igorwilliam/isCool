from django.db import models

# Create your models here.

class Material(models.Model):

    discipline = models.ForeignKey('discipline.Discipline', verbose_name='Disciplina', on_delete=models.PROTECT)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descição', blank=True)
    file = models.FileField('Material', upload_to='materials')
    shared_by = models.ForeignKey('accounts.User', verbose_name='Compartilhado por', on_delete=models.PROTECT)



    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'
