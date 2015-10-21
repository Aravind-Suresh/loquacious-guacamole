# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiit', '0009_auto_20151019_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tshirt_size',
            field=models.CharField(blank=True, max_length=5, null=True, choices=[(b's', b'S'), (b'm', b'M'), (b'l', b'L'), (b'xl', b'XL'), (b'xxl', b'XXL')]),
        ),
    ]
