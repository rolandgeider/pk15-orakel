# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('oracle', '0006_auto_20140921_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coordinates', models.ForeignKey(verbose_name=b'Koordinate', to='oracle.Coordinate')),
                ('question', models.ForeignKey(verbose_name=b'Frage', to='oracle.Question')),
                ('team', models.ForeignKey(verbose_name=b'Frage', to='core.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
