# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interiit', '0005_auto_20150914_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='sport',
            field=models.CharField(blank=True, max_length=25, null=True, choices=[(b'athletics', b'Athletics'), (b'badminton', b'Badminton'), (b'basket ball', b'Basket Ball'), (b'cricket', b'Cricket'), (b'football', b'Football'), (b'hockey', b'Hockey'), (b'squash', b'Squash'), (b'swimming', b'Swimming'), (b'table tennis', b'Table Tennis'), (b'tennis', b'Tennis'), (b'volley ball', b'Volley Ball'), (b'water polo', b'Water Polo'), (b'weight lifting', b'Weight Lifting')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='event1',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'50 M Freestyle', b'50 M Freestyle'), (b'100 M Freestyle', b'100 M Freestyle'), (b'200 M Freestyle', b'200 M Freestyle'), (b'400 M Freestyle', b'400 M Freestyle'), (b'1500 M Freestyle', b'1500 M Freestyle'), (b'50 M Breast Stroke', b'50 M Breast Stroke'), (b'100 M Breast Stroke', b'100 M Breast Stroke'), (b'200 M Breast Stroke', b'200 M Breast Stroke'), (b'50 M Back Stroke', b'50 M Back Stroke'), (b'100 M Back stroke', b'100 M Back stroke'), (b'200 M stroke', b'200 M stroke'), (b'50 M Butterfly', b'50 M Butterfly'), (b'100 M Butterfly', b'100 M Butterfly'), (b'200 M Individual Medley', b'200 M Individual Medley')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='event2',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'50 M Freestyle', b'50 M Freestyle'), (b'100 M Freestyle', b'100 M Freestyle'), (b'200 M Freestyle', b'200 M Freestyle'), (b'400 M Freestyle', b'400 M Freestyle'), (b'1500 M Freestyle', b'1500 M Freestyle'), (b'50 M Breast Stroke', b'50 M Breast Stroke'), (b'100 M Breast Stroke', b'100 M Breast Stroke'), (b'200 M Breast Stroke', b'200 M Breast Stroke'), (b'50 M Back Stroke', b'50 M Back Stroke'), (b'100 M Back stroke', b'100 M Back stroke'), (b'200 M stroke', b'200 M stroke'), (b'50 M Butterfly', b'50 M Butterfly'), (b'100 M Butterfly', b'100 M Butterfly'), (b'200 M Individual Medley', b'200 M Individual Medley')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='event3',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'50 M Freestyle', b'50 M Freestyle'), (b'100 M Freestyle', b'100 M Freestyle'), (b'200 M Freestyle', b'200 M Freestyle'), (b'400 M Freestyle', b'400 M Freestyle'), (b'1500 M Freestyle', b'1500 M Freestyle'), (b'50 M Breast Stroke', b'50 M Breast Stroke'), (b'100 M Breast Stroke', b'100 M Breast Stroke'), (b'200 M Breast Stroke', b'200 M Breast Stroke'), (b'50 M Back Stroke', b'50 M Back Stroke'), (b'100 M Back stroke', b'100 M Back stroke'), (b'200 M stroke', b'200 M stroke'), (b'50 M Butterfly', b'50 M Butterfly'), (b'100 M Butterfly', b'100 M Butterfly'), (b'200 M Individual Medley', b'200 M Individual Medley')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='relay_event1',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'4x50 Freestyle Relay', b'4x50 Freestyle Relay'), (b'4x100 Freestyle Relay', b'4x100 Freestyle Relay'), (b'4x100 Medley Relay', b'4x100 Medley Relay')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='relay_event2',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'4x50 Freestyle Relay', b'4x50 Freestyle Relay'), (b'4x100 Freestyle Relay', b'4x100 Freestyle Relay'), (b'4x100 Medley Relay', b'4x100 Medley Relay')]),
        ),
    ]
