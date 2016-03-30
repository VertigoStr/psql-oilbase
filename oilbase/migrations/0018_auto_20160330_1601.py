# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilbase', '0017_contact_slogans'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='coordinats',
            field=models.CharField(max_length=100, null=True, verbose_name='Координаты'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=250, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Адрес электронной почты'),
        ),
    ]
