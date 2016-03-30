# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0010_auto_20160330_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='Имя', max_length=100)),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AlterModelOptions(
            name='deliver',
            options={'verbose_name': 'Поставка', 'verbose_name_plural': 'Поставки'},
        ),
        migrations.AlterModelOptions(
            name='dilers',
            options={'verbose_name': 'Дилеры', 'verbose_name_plural': 'Дилеры'},
        ),
        migrations.AlterField(
            model_name='deliver',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='deliver',
            name='first_image',
            field=models.ImageField(verbose_name='Изображение №1', upload_to='./media/img/'),
        ),
        migrations.AlterField(
            model_name='deliver',
            name='second_image',
            field=models.ImageField(verbose_name='Изображение №2', upload_to='./media/img/'),
        ),
        migrations.AlterField(
            model_name='deliver',
            name='third_image',
            field=models.ImageField(verbose_name='Изображение №3', upload_to='./media/img/'),
        ),
        migrations.AlterField(
            model_name='deliver',
            name='title',
            field=models.CharField(verbose_name='Имя', max_length=100),
        ),
        migrations.AlterField(
            model_name='dilers',
            name='address',
            field=models.CharField(verbose_name='Адрес', max_length=250),
        ),
        migrations.AlterField(
            model_name='dilers',
            name='city',
            field=models.CharField(verbose_name='Город', max_length=50),
        ),
        migrations.AlterField(
            model_name='dilers',
            name='email',
            field=models.EmailField(verbose_name='Почта', max_length=254),
        ),
        migrations.AlterField(
            model_name='dilers',
            name='phone',
            field=models.CharField(verbose_name='Телефон', max_length=20),
        ),
    ]
