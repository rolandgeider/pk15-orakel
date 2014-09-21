# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0015_auto_20140921_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerconfig',
            name='is_wrong',
            field=models.BooleanField(default=False, verbose_name=b'Falsche Antwort'),
            preserve_default=True,
        ),
    ]
