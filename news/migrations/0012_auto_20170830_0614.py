# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 06:14
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0011_auto_20170830_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title',
                                                unique_with=['title']),
        ),
    ]
