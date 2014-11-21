# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='choices',
            field=models.CharField(default='', max_length=1500),
            preserve_default=True,
        ),
    ]
