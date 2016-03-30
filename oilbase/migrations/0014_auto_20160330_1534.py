# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0013_auto_20160330_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departaments',
            options={'verbose_name_plural': 'Отделы', 'verbose_name': 'Отдел'},
        ),
        migrations.AddField(
            model_name='dilers',
            name='coordinats',
            field=models.CharField(null=True, max_length=100, verbose_name='Координаты'),
        ),
    ]
