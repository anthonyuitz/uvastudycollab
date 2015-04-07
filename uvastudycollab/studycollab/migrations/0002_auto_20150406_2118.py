# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studycollab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='users',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
