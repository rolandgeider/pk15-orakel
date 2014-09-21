# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0011_auto_20140921_1212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coordinate',
            options={'ordering': ['description']},
        ),
        migrations.RemoveField(
            model_name='questionconfig',
            name='uuid',
        ),
        migrations.AddField(
            model_name='coordinate',
            name='uuid',
            field=models.CharField(default='e59ad929-0167-44b8-8b35-483969ca3602', max_length=36, verbose_name=b'UUID'),
            preserve_default=False,
        ),
    ]
