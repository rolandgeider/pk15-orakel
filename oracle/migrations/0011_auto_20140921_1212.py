# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0010_questionconfig_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionconfig',
            name='uuid',
            field=models.CharField(max_length=36, verbose_name=b'UUID'),
        ),
    ]
