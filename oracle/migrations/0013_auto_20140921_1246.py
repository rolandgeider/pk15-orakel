# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0012_auto_20140921_1240'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='questionconfig',
            unique_together=set([('team', 'coordinate')]),
        ),
    ]
