# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiit', '0006_auto_20150914_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='event1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='event2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='event3',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='relay_event1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='relay_event2',
        ),
        migrations.AddField(
            model_name='profile',
            name='event',
            field=models.CharField(blank=True, max_length=35, null=True, choices=[(b'100 M', b'100 M'), (b'200 M', b'200 M'), (b'400 M', b'400 M'), (b'400 M', b'400 M'), (b'800 M', b'800 M'), (b'1500 M', b'1500 M'), (b'5000 M', b'5000 M'), (b'110 M Hurdles', b'110 M Breast Stroke'), (b'400 M Hurdles', b'400 M Hurdles'), (b'High Jump', b'High Jump'), (b'Long Jump', b'Long Jump'), (b'Triple Jump', b'Triple Jump'), (b'Pole Vault', b'Pole Vault'), (b'Shot Put', b'Shot Put'), (b'Discuss Throw', b'Discuss Throw'), (b'Javelin Throw', b'Javelin Throw'), (b'Hammer Throw', b'Hammer Throw'), (b'4x100 M Relay', b'4x100 M Relay'), (b'4x400 M Relay', b'4x400 M Relay')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='food_preference',
            field=models.CharField(max_length=20, choices=[(b'veg', b'Vegetarian'), (b'nonveg', b'Non Vegetarian'), (b'jain', b'jain')]),
        ),
    ]
