# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0004_userprofile_locked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='rollnumber',
            new_name='uniqueid',
        ),
    ]
