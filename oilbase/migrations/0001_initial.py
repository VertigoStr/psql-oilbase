# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dilers',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('diler_id', models.IntegerField()),
                ('city', models.TextField()),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
