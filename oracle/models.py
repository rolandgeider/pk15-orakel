# -*- coding: utf-8 -*-

# This file is part of pk15 Orakel
#
# pk15 Orakel is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pk15 Orakel is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License


from django.db import models
from core.models import Team


class Log(models.Model):
    '''
    Model for a GPS log entry
    '''

    team = models.ForeignKey(Team)
    '''
    Team this entry belongs to
    '''

    lat = models.FloatField()
    lon = models.FloatField()

    def get_owner_object(self):
        '''
        Needed for generic views, not used
        '''
        return None

    def __unicode__(self):
        return self.name


class Coordinate(models.Model):
    '''
    A geographical point, used for questions
    '''
    description = models.CharField(verbose_name=u'Beschreibung',
                                   help_text=u'Wird nur im Admininterface verwendet',
                                   max_length=30)
    lat = models.FloatField()
    lon = models.FloatField()

    def get_owner_object(self):
        '''
        Needed for generic views, not used
        '''
        return None

    def __unicode__(self):
        return self.description


class Question(models.Model):
    '''
    A question
    '''
    team = models.ForeignKey(Team, verbose_name='Team')
    '''
    Team this question belongs to
    '''

    question = models.TextField(verbose_name='Frage')
    '''
    Actual question
    '''

    def get_owner_object(self):
        '''
        Needed for generic views, not used
        '''
        return None

    def __unicode__(self):
        return self.question[:15]


class Answer(models.Model):
    '''
    An answer to a question
    '''
    question = models.ForeignKey(Question, verbose_name='Frage')
    '''
    Question this answer belongs to
    '''

    answer = models.TextField(verbose_name='Antwort')
    '''
    Actual question
    '''

    lat = models.FloatField()
    long = models.FloatField()
