# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import interiit.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sport', models.CharField(blank=True, max_length=25, null=True, choices=[(b'athletics', b'Athletics'), (b'badminton', b'Badminton'), (b'basketball', b'BasketBall'), (b'cricket', b'Cricket'), (b'football', b'Football'), (b'hockey', b'Hockey'), (b'squash', b'Squash'), (b'swimming', b'Swimming'), (b'tabletennis', b'TableTennis'), (b'tennis', b'Tennis'), (b'volleyball', b'VolleyBall'), (b'waterpolo', b'WaterPolo'), (b'weightlifting', b'Weightlifting')])),
                ('college', models.CharField(max_length=25, null=True, blank=True)),
                ('user', models.ForeignKey(related_name='detail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('middle_name', models.CharField(max_length=25, null=True, blank=True)),
                ('last_name', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('date_of_birth', models.DateTimeField()),
                ('bood_group', models.CharField(max_length=5)),
                ('Roll_number', models.CharField(max_length=10)),
                ('events', models.CharField(max_length=25, choices=[(b'a', b'A'), (b'b', b'B')])),
                ('phone_number', models.CharField(max_length=10)),
                ('parents_phone_number', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to=interiit.models.get_upload_path, blank=True)),
                ('food_preference', models.CharField(max_length=20, choices=[(b'veg', b'Vegetarian'), (b'nonveg', b'Non Vegetarian')])),
                ('tshirt_size', models.CharField(max_length=5, choices=[(b's', b'S'), (b'm', b'M'), (b'l', b'L'), (b'xl', b'XL'), (b'xxl', b'XXL')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
