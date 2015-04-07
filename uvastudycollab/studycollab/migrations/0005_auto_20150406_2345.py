# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studycollab', '0004_auto_20150406_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='groupName',
            new_name='className',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='users',
            new_name='groups',
        ),
    ]
