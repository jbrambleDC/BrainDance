# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trailio', '0004_auto_20150926_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
