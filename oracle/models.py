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
from django.core.urlresolvers import reverse

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
    class Meta:
        '''
        Configure other properties
        '''
        ordering = ["-is_jail", "description", ]

    description = models.CharField(verbose_name=u'Beschreibung',
                                   help_text=u'Wird nur im Admininterface verwendet',
                                   max_length=30)
    lat = models.FloatField()
    lon = models.FloatField()

    is_jail = models.BooleanField(verbose_name=u"Ist Strafort",
                                  help_text=u"Wird bei falschen Antworten verwendet",
                                  default=False)

    uuid = models.CharField(verbose_name='UUID',
                            max_length=36)

    def get_absolute_url(self):
        return reverse('oracle:coordinate-detail', kwargs={'pk': self.pk})

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
        return u"#{0} - {1}".format(self.pk, self.question[:25])


class Answer(models.Model):
    '''
    An answer to a question
    '''
    class Meta:
        '''
        Configure other properties
        '''
        ordering = ["?", ]

    question = models.ForeignKey(Question, verbose_name='Frage')
    '''
    Question this answer belongs to
    '''

    answer = models.CharField(verbose_name='Antwort',
                              max_length=50)
    '''
    Answer
    '''

    is_wrong = models.BooleanField(verbose_name='Falsche Antwort',
                                   help_text=u"falsche Antwort, schickt das Team zur Intevation",
                                   default=False)

    def get_owner_object(self):
        '''
        Needed for generic views, not used
        '''
        return None

    def __unicode__(self):
        return self.answer


class QuestionConfig(models.Model):
    '''
    A configured question
    '''

    class Meta:
        '''
        Configure other properties
        '''
        ordering = ["team", "id", "-question"]
        unique_together = (
                            ('team', 'coordinate'),
                            ('team', 'question')
                          )
    team = models.ForeignKey(Team,
                             verbose_name='Team')
    
    question = models.ForeignKey(Question,
                                 verbose_name='Frage')

    coordinate = models.ForeignKey(Coordinate,
                                   verbose_name='Koordinate')

    def get_owner_object(self):
        '''
        Needed for generic views, not used
        '''
        return None

    def __unicode__(self):
        return "#{0}".format(self.pk)


class AnswerConfig(models.Model):
    '''
    A configured answer
    '''

    question_config = models.ForeignKey(QuestionConfig,
                                        verbose_name='Teamfrage',
                                        editable=False)

    answer = models.ForeignKey(Answer,
                               verbose_name='Antwort',
                               editable=False)

    next_coordinate = models.ForeignKey(Coordinate,
                                        verbose_name='Nächste Koordinate',
                                        null=True,
                                        blank=True)

    def get_owner_object(self):
        '''
        Needed for generic views, not used
        '''
        return None

    def __unicode__(self):
        return u"#{0} - {1}".format(self.pk, self.answer)


class TeamAnswerLog(models.Model):
    '''
    The answer to a question given by a team
    '''

    class Meta:
        '''
        Configure other properties
        '''
        ordering = ["time", ]

    team = models.ForeignKey(Team)
    question_config = models.ForeignKey(QuestionConfig)
    team_answer = models.ForeignKey(Answer)
    place = models.TextField()
    reference = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def get_owner_object(self):
        '''
        Needed for generic views, not used
        '''
        return None

    def __unicode__(self):
        return "#{0}".format(self.pk)
