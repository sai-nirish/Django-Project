# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0005_auto_20141027_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='uniqueid',
            field=models.CharField(max_length=10, unique=True),
            preserve_default=True,
        ),
    ]
