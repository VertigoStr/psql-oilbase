# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallBack',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('coordinats', models.CharField(max_length=100, verbose_name='Координаты', null=True)),
                ('site', models.CharField(max_length=20, verbose_name='Сайт')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('first_image', models.ImageField(verbose_name='Изображение №1', upload_to='./media/img/')),
                ('second_image', models.ImageField(verbose_name='Изображение №2', upload_to='./media/img/')),
                ('third_image', models.ImageField(verbose_name='Изображение №3', upload_to='./media/img/')),
            ],
            options={
                'verbose_name': 'Поставка',
                'verbose_name_plural': 'Поставки',
            },
        ),
        migrations.CreateModel(
            name='Departaments',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Имя')),
                ('worktime', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), size=7, blank=True, verbose_name='График работы')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='Dilers',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('city', models.CharField(max_length=50, verbose_name='Область')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('coordinats', models.CharField(max_length=100, verbose_name='Координаты', null=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Дилеры',
                'verbose_name_plural': 'Дилеры',
            },
        ),
        migrations.CreateModel(
            name='MainPageContent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('img', models.ImageField(upload_to='./media/img/', verbose_name='Изображение', null=True)),
            ],
            options={
                'verbose_name': 'Элемент',
                'verbose_name_plural': 'Элементы',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('post', models.CharField(max_length=100, verbose_name='Должность')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('departament', models.ForeignKey(to='oilbase.Departaments', verbose_name='Отдел')),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонал',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Имя')),
                ('image', models.ImageField(verbose_name='Изображение', upload_to='./media/img/')),
                ('description', models.CharField(max_length=250, verbose_name='Описание')),
                ('content', models.CharField(max_length=100, verbose_name='Емкость')),
                ('gost', models.CharField(max_length=250, verbose_name='ГОСТ')),
                ('docs', models.CharField(max_length=350, verbose_name='Паспорт качества')),
                ('cost', models.IntegerField(verbose_name='Цена')),
                ('category', models.ForeignKey(to='oilbase.Categories', verbose_name='Категория')),
                ('send_type', models.ForeignKey(to='oilbase.Deliver', verbose_name='Вид доставки')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Slogans',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
                ('page', models.CharField(max_length=100, verbose_name='Страница', null=True)),
            ],
            options={
                'verbose_name': 'Слоган',
                'verbose_name_plural': 'Слоганы',
            },
        ),
    ]
