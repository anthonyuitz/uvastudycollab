# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studycollab', '0009_studygroup_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studygroup',
            name='owner',
        ),
    ]
