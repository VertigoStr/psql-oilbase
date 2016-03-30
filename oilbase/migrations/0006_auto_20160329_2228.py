# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0005_auto_20160329_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliver',
            name='first_image',
            field=models.ImageField(upload_to='/static/img'),
        ),
        migrations.AlterField(
            model_name='deliver',
            name='second_image',
            field=models.ImageField(upload_to='/static/img'),
        ),
        migrations.AlterField(
            model_name='deliver',
            name='third_image',
            field=models.ImageField(upload_to='/static/img'),
        ),
    ]
