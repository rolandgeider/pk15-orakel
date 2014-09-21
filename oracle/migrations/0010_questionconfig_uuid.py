# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0009_auto_20140921_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionconfig',
            name='uuid',
            field=models.CharField(default='e59ad929-0167-44b8-8b35-483969ca3602', max_length=32, verbose_name=b'UUID'),
            preserve_default=False,
        ),
    ]
