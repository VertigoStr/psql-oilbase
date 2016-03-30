# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0006_auto_20160329_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliver',
            name='first_image',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='deliver',
            name='second_image',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='deliver',
            name='third_image',
            field=models.CharField(max_length=100),
        ),
    ]
