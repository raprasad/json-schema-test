# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-25 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata_organizer', '0002_metadataschema_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadataschema',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
