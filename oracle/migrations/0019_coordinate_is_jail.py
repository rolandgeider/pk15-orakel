# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0018_teamanswerlog_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinate',
            name='is_jail',
            field=models.BooleanField(default=False, help_text='Wird bei falschen Antworten verwendet', verbose_name='Ist Strafort'),
            preserve_default=True,
        ),
    ]
