# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studycollab', '0017_help_category_help_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='help_question',
            name='category',
            field=models.ForeignKey(default=1, to='studycollab.help_category'),
            preserve_default=False,
        ),
    ]
