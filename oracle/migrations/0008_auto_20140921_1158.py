# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0007_questionconfig'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionconfig',
            options={'ordering': ['team', 'question']},
        ),
        migrations.RenameField(
            model_name='questionconfig',
            old_name='coordinates',
            new_name='coordinate',
        ),
        migrations.AlterField(
            model_name='questionconfig',
            name='team',
            field=models.ForeignKey(verbose_name=b'Team', to='core.Team'),
        ),
    ]
