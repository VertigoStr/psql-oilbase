# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0020_auto_20160330_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpagecontent',
            name='img',
            field=models.ImageField(upload_to='./media/img/', null=True, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='slogans',
            name='page',
            field=models.CharField(max_length=100, null=True, verbose_name='Страница'),
        ),
    ]
