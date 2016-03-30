# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0019_auto_20160330_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageContent',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Элемент',
                'verbose_name_plural': 'Элементы',
            },
        ),
        migrations.AddField(
            model_name='slogans',
            name='page',
            field=models.CharField(max_length=100, verbose_name='Страница отображения', null=True),
        ),
    ]
