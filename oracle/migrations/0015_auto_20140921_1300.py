# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0014_answerconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerconfig',
            name='next_coordinate',
            field=models.ForeignKey(verbose_name=b'N\xc3\xa4chste Koordinate', blank=True, to='oracle.Coordinate', null=True),
        ),
    ]
