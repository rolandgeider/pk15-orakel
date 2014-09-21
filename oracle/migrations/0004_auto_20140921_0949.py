# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0003_coordinates'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coordinates',
            new_name='Coordinate',
        ),
    ]
