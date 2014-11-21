# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0002_userprofile_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='category',
            field=models.CharField(max_length=2, default='GE'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pdstatus',
            field=models.CharField(max_length=1, default='N'),
            preserve_default=True,
        ),
    ]
