# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0014_auto_20160330_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('post', models.CharField(max_length=100, verbose_name='Должность')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('departament', models.ForeignKey(to='oilbase.Departaments', verbose_name='Отдел')),
            ],
            options={
                'verbose_name_plural': 'Персонал',
                'verbose_name': 'Персонал',
            },
        ),
    ]
