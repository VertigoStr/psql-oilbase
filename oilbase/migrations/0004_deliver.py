# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0003_remove_dilers_diler_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('first_image', models.ImageField(upload_to='')),
                ('second_image', models.ImageField(upload_to='')),
                ('third_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
