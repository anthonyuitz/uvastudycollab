# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studycollab', '0003_auto_20150406_2136'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='groups',
            new_name='group',
        ),
    ]
