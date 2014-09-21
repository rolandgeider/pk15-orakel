# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0002_auto_20140921_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(help_text='Wird nur im Admininterface verwendet', max_length=30, verbose_name='Beschreibung')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
