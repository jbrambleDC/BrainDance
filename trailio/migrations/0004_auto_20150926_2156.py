# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trailio', '0003_location_region_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infographic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('infographic_image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(null=True, blank=True)),
                ('Prefered', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 9, 26, 21, 56, 17, 776766))),
                ('location', models.ManyToManyField(to='trailio.Location')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='begin_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='end_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateTimeField(default=datetime.datetime(1900, 1, 1, 12, 0), blank=True),
        ),
        migrations.AddField(
            model_name='route',
            name='user',
            field=models.ForeignKey(to='trailio.User'),
        ),
        migrations.AddField(
            model_name='preference',
            name='activity',
            field=models.ForeignKey(to='trailio.Activity'),
        ),
        migrations.AddField(
            model_name='preference',
            name='user',
            field=models.ForeignKey(to='trailio.User'),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='activity',
            field=models.ManyToManyField(to='trailio.Activity'),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='route',
            field=models.OneToOneField(to='trailio.Route'),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='user',
            field=models.ForeignKey(to='trailio.User'),
        ),
        migrations.AddField(
            model_name='infographic',
            name='itinerary',
            field=models.OneToOneField(to='trailio.Itinerary'),
        ),
    ]
