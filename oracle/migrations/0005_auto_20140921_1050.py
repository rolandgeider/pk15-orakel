# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0004_auto_20140921_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='long',
        ),
        migrations.RemoveField(
            model_name='question',
            name='team',
        ),
    ]
