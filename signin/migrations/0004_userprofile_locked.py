# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0003_auto_20141027_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='locked',
            field=models.CharField(default='N', max_length=1),
            preserve_default=True,
        ),
    ]
