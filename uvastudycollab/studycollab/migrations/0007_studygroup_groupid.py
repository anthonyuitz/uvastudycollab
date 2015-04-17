# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('studycollab', '0006_auto_20150417_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='studygroup',
            name='groupid',
            field=models.CharField(default=datetime.datetime(2015, 4, 17, 4, 4, 7, 390106, tzinfo=utc), unique=True, max_length=10),
            preserve_default=False,
        ),
    ]
