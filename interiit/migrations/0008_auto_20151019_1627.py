# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiit', '0007_auto_20151017_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='participant_type',
            field=models.CharField(max_length=35, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='staff_type',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'Coach', b'Coach'), (b'Professor', b'Professor'), (b'Sports Officer', b'Sports Officer')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='event',
            field=models.CharField(max_length=35, null=True, blank=True),
        ),
    ]
