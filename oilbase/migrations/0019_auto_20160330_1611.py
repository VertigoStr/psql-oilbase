# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0018_auto_20160330_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dilers',
            name='city',
            field=models.CharField(verbose_name='Область', max_length=50),
        ),
    ]
