# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0017_auto_20140921_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamanswerlog',
            name='time',
            field=models.DateTimeField(default=datetime.date(2014, 9, 22), auto_now_add=True),
            preserve_default=False,
        ),
    ]
