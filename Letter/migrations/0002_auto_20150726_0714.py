# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Letter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='date_received',
            field=models.DateTimeField(verbose_name='Deliver on:'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='privacy',
            field=models.BooleanField(verbose_name='Private'),
        ),
    ]
