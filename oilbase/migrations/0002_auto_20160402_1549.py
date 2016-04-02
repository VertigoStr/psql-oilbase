# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='docs',
            field=models.CharField(verbose_name='Паспорт качества', max_length=250),
        ),
        migrations.AlterField(
            model_name='products',
            name='send_type',
            field=models.ForeignKey(verbose_name='Тип доставки', to='oilbase.Deliver'),
        ),
    ]
