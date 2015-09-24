# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interiit', '0003_auto_20150910_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Roll_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='blood_group',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='event1',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'a', b'A'), (b'b', b'B')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='event2',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'a', b'A'), (b'b', b'B')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='event3',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'a', b'A'), (b'b', b'B')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='event4',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'a', b'A'), (b'b', b'B')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='event5',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'a', b'A'), (b'b', b'B')]),
        ),
    ]
