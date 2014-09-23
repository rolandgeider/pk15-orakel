# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0019_coordinate_is_jail'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='questionconfig',
            unique_together=set([('team', 'question'), ('team', 'coordinate')]),
        ),
    ]
