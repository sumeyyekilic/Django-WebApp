# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-02 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gonderi', '0002_auto_20190612_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='gonderi',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]