# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0002_auto_20160329_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dilers',
            name='diler_id',
        ),
    ]
