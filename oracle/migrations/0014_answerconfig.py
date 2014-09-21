# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0013_auto_20140921_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.ForeignKey(editable=False, to='oracle.Answer', verbose_name=b'Antwort')),
                ('next_coordinate', models.ForeignKey(verbose_name=b'N\xc3\xa4chste Koordinate', to='oracle.Coordinate')),
                ('question_config', models.ForeignKey(editable=False, to='oracle.QuestionConfig', verbose_name=b'Teamfrage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
