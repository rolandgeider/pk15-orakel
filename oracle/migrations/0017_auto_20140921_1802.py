# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('oracle', '0016_answerconfig_is_wrong'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamAnswerLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.TextField()),
                ('reference', models.TextField()),
                ('question_config', models.ForeignKey(to='oracle.QuestionConfig')),
                ('team', models.ForeignKey(to='core.Team')),
                ('team_answer', models.ForeignKey(to='oracle.Answer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='answerconfig',
            options={'ordering': ['is_wrong']},
        ),
        migrations.AlterModelOptions(
            name='questionconfig',
            options={'ordering': ['team', '-question']},
        ),
        migrations.AlterField(
            model_name='answerconfig',
            name='is_wrong',
            field=models.BooleanField(default=False, help_text='falsche Antwort, schickt das Team zur Intevation', verbose_name=b'Falsche Antwort'),
        ),
    ]
