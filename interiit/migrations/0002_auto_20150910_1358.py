# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interiit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='events',
        ),
        migrations.AddField(
            model_name='profile',
            name='event1',
            field=models.CharField(blank=True, max_length=25, null=True, choices=[(b'a', b'A'), (b'b', b'B')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='event2',
            field=models.CharField(blank=True, max_length=25, null=True, choices=[(b'a', b'A'), (b'b', b'B')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='event3',
            field=models.CharField(blank=True, max_length=25, null=True, choices=[(b'a', b'A'), (b'b', b'B')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='event4',
            field=models.CharField(blank=True, max_length=25, null=True, choices=[(b'a', b'A'), (b'b', b'B')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='event5',
            field=models.CharField(blank=True, max_length=25, null=True, choices=[(b'a', b'A'), (b'b', b'B')]),
        ),
    ]
