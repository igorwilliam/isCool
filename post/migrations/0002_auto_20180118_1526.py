# Generated by Django 2.0.1 on 2018-01-18 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-created'], 'verbose_name': 'Tópico', 'verbose_name_plural': 'Tópicos'},
        ),
        migrations.RemoveField(
            model_name='topic',
            name='topic',
        ),
        migrations.AddField(
            model_name='reply',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='post.Topic', verbose_name='Tópico'),
            preserve_default=False,
        ),
    ]
