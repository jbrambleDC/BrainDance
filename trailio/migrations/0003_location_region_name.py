# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trailio', '0002_auto_20150906_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='region_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
