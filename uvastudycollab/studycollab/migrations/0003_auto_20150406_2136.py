# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studycollab', '0002_auto_20150406_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('users', models.CharField(max_length=1000, blank=True)),
                ('groupName', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='group',
        ),
    ]
