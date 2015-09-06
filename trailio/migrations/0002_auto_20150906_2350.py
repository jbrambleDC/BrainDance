# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trailio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_weather',
            field=models.CharField(default=b'MILD', max_length=20),
        ),
        migrations.AddField(
            model_name='activity',
            name='begin_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='end_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='weather',
            field=models.CharField(default=b'MILD', max_length=8, choices=[(b'WARM', b'WARM'), (b'MILD', b'MILD'), (b'COLD', b'COLD'), (b'HOT', b'HOT'), (b'TROPICAL', b'TROPICAL')]),
        ),
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateTimeField(default=b'1900-01-01', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=b'0', max_length=20),
        ),
    ]
