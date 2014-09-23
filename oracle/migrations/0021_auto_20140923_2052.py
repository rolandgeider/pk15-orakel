# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0020_auto_20140923_1513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['is_wrong']},
        ),
        migrations.AlterModelOptions(
            name='answerconfig',
            options={},
        ),
        migrations.RemoveField(
            model_name='answerconfig',
            name='is_wrong',
        ),
        migrations.AddField(
            model_name='answer',
            name='is_wrong',
            field=models.BooleanField(default=False, help_text='falsche Antwort, schickt das Team zur Intevation', verbose_name=b'Falsche Antwort'),
            preserve_default=True,
        ),
    ]
