# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dilers',
            name='address',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='dilers',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]
