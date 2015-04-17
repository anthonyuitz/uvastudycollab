# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studycollab', '0015_document_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='file',
            new_name='document',
        ),
    ]
