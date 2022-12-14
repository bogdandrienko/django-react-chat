# Generated by Django 4.1 on 2022-08-07 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TextModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, default='', help_text='<small class="text-muted">это наше сообщение</small><hr><br>', max_length=500, null=True, verbose_name='текст сообщения:')),
                ('created_datetime', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='<small class="text-muted">время создания</small><hr><br>', null=True, verbose_name='время создания:')),
                ('author', models.ForeignKey(blank=True, default=None, help_text='<small class="text-muted">Автор</small><hr><br>', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ('text',),
            },
        ),
    ]
