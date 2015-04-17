# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studycollab', '0007_studygroup_groupid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studygroup',
            name='groupid',
            field=models.CharField(unique=True, max_length=10, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
