# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interiit', '0004_auto_20150911_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='event4',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='event5',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='relay_event1',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'None', b'None'), (b'4x50 Freestyle Relay', b'4x50 Freestyle Relay'), (b'4x100 Freestyle Relay', b'4x100 Freestyle Relay'), (b'4x100 Medley Relay', b'4x100 Medley Relay')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='relay_event2',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'None', b'None'), (b'4x50 Freestyle Relay', b'4x50 Freestyle Relay'), (b'4x100 Freestyle Relay', b'4x100 Freestyle Relay'), (b'4x100 Medley Relay', b'4x100 Medley Relay')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='event1',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'None', b'None'), (b'50 M Freestyle', b'50 M Freestyle'), (b'100 M Freestyle', b'100 M Freestyle'), (b'200 M Freestyle', b'200 M Freestyle'), (b'400 M Freestyle', b'400 M Freestyle'), (b'1500 M Freestyle', b'1500 M Freestyle'), (b'50 M Breast Stroke', b'50 M Breast Stroke'), (b'100 M Breast Stroke', b'100 M Breast Stroke'), (b'200 M Breast Stroke', b'200 M Breast Stroke'), (b'50 M Back Stroke', b'50 M Back Stroke'), (b'100 M Back stroke', b'100 M Back stroke'), (b'200 M stroke', b'200 M stroke'), (b'50 M Butterfly', b'50 M Butterfly'), (b'100 M Butterfly', b'100 M Butterfly'), (b'200 M Individual Medley', b'200 M Individual Medley')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='event2',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'None', b'None'), (b'50 M Freestyle', b'50 M Freestyle'), (b'100 M Freestyle', b'100 M Freestyle'), (b'200 M Freestyle', b'200 M Freestyle'), (b'400 M Freestyle', b'400 M Freestyle'), (b'1500 M Freestyle', b'1500 M Freestyle'), (b'50 M Breast Stroke', b'50 M Breast Stroke'), (b'100 M Breast Stroke', b'100 M Breast Stroke'), (b'200 M Breast Stroke', b'200 M Breast Stroke'), (b'50 M Back Stroke', b'50 M Back Stroke'), (b'100 M Back stroke', b'100 M Back stroke'), (b'200 M stroke', b'200 M stroke'), (b'50 M Butterfly', b'50 M Butterfly'), (b'100 M Butterfly', b'100 M Butterfly'), (b'200 M Individual Medley', b'200 M Individual Medley')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='event3',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'None', b'None'), (b'50 M Freestyle', b'50 M Freestyle'), (b'100 M Freestyle', b'100 M Freestyle'), (b'200 M Freestyle', b'200 M Freestyle'), (b'400 M Freestyle', b'400 M Freestyle'), (b'1500 M Freestyle', b'1500 M Freestyle'), (b'50 M Breast Stroke', b'50 M Breast Stroke'), (b'100 M Breast Stroke', b'100 M Breast Stroke'), (b'200 M Breast Stroke', b'200 M Breast Stroke'), (b'50 M Back Stroke', b'50 M Back Stroke'), (b'100 M Back stroke', b'100 M Back stroke'), (b'200 M stroke', b'200 M stroke'), (b'50 M Butterfly', b'50 M Butterfly'), (b'100 M Butterfly', b'100 M Butterfly'), (b'200 M Individual Medley', b'200 M Individual Medley')]),
        ),
    ]
