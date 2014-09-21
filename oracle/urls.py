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


from django.conf.urls import patterns, url

from oracle.views import question
from oracle.views import question_config
from oracle.views import answer
from oracle.views import answer_config
from oracle.views import coordinate
from oracle.views import misc


urlpatterns = patterns('',

    # Index
    url(r'^dashboard$',
        misc.dashboard,
        name='dashboard'),

    # Coordinates
    url(r'^koordinate/(?P<uuid>[0-9a-f-]{1,36})$',
        misc.check_step,
        name='check-step'),
    url(r'^koordinate/liste$',
        coordinate.CoordinateListView.as_view(),
        name='coordinate-list'),
    url(r'^koordinate/hinzufuegen',
        coordinate.CoordinateAddView.as_view(),
        name='coordinate-add'),
    url(r'^koordinate/(?P<pk>\d+)/bearbeiten',
        coordinate.CoordinateUpdateView.as_view(),
        name='coordinate-edit'),
    url(r'^koordinate/(?P<pk>\d+)/anzeigen',
        coordinate.CoordinateDetaillView.as_view(),
        name='coordinate-detail'),
    url(r'^koordinate/(?P<pk>\d+)/loeschen',
        coordinate.CoordinateDeleteView.as_view(),
        name='coordinate-delete'),

    # Questions
    url(r'^frage/liste$',
        question.QuestionListView.as_view(),
        name='question-list'),
    url(r'^frage/hinzufuegen',
        question.QuestionAddView.as_view(),
        name='question-add'),
    url(r'^frage/(?P<pk>\d+)/bearbeiten',
        question.QuestionUpdateView.as_view(),
        name='question-edit'),
    url(r'^frage/(?P<pk>\d+)/anzeigen',
        question.QuestionDeatilView.as_view(),
        name='question-detail'),
    url(r'^frage/(?P<pk>\d+)/loeschen',
        question.QuestionDeleteView.as_view(),
        name='question-delete'),

    # Answers
    url(r'^antwort/hinzufuegen',
        answer.AnswerAddView.as_view(),
        name='answer-add'),
    url(r'^antwort/(?P<pk>\d+)/bearbeiten',
        answer.AnswerUpdateView.as_view(),
        name='answer-edit'),
    url(r'^antwort/(?P<pk>\d+)/loeschen',
        answer.AnswerDeleteView.as_view(),
        name='answer-delete'),

    # Answer configs
    url(r'^antwort-konfig/(?P<pk>\d+)/bearbeiten',
        answer_config.AnswerConfigUpdateView.as_view(),
        name='answer-config-edit'),
    
    
    # Question configs
    url(r'^frage-konfig/liste$',
        question_config.QuestionConfigListView.as_view(),
        name='question-config-list'),
    url(r'^frage-konfig/hinzufuegen',
        question_config.QuestionConfigAddView.as_view(),
        name='question-config-add'),
    url(r'^frage-konfig/(?P<pk>\d+)/bearbeiten',
        question_config.QuestionConfigUpdateView.as_view(),
        name='question-config-edit'),
    url(r'^frage-konfig/(?P<pk>\d+)/anzeigen',
        question_config.QuestionConfigDeatilView.as_view(),
        name='question-config-detail'),
    url(r'^frage-konfig/(?P<pk>\d+)/loeschen',
        question_config.QuestionConfigDeleteView.as_view(),
        name='question-config-delete'),

)