# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0012_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departaments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Имя')),
                ('worktime', django.contrib.postgres.fields.ArrayField(blank=True, base_field=models.CharField(max_length=15), size=7, verbose_name='График работы')),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(to='oilbase.Categories', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='products',
            name='cost',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
