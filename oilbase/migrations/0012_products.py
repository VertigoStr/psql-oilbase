# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0011_auto_20160330_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Имя', max_length=100)),
                ('image', models.ImageField(upload_to='./media/img/', verbose_name='Изображение')),
                ('description', models.CharField(verbose_name='Описание', max_length=250)),
                ('send_type', models.CharField(verbose_name='Тип доставки', max_length=100)),
                ('content', models.CharField(verbose_name='Емкость', max_length=100)),
                ('gost', models.CharField(verbose_name='ГОСТ', max_length=250)),
                ('docs', models.CharField(verbose_name='Паспорт качества', max_length=250)),
                ('cost', models.IntegerField()),
                ('category', models.ForeignKey(to='oilbase.Categories')),
            ],
            options={
                'verbose_name_plural': 'Товары',
                'verbose_name': 'Товар',
            },
        ),
    ]
