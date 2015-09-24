# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interiit', '0002_auto_20150910_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bood_group',
            new_name='blood_group',
        ),
    ]
