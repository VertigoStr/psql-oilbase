# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0016_callback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес электронной почты')),
                ('site', models.CharField(max_length=20, verbose_name='Сайт')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Slogans',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Слоган',
                'verbose_name_plural': 'Слоганы',
            },
        ),
    ]
