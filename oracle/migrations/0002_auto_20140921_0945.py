# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='long',
            new_name='lon',
        ),
    ]
