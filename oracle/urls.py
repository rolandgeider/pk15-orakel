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
from django.views.generic import TemplateView

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
    url(r'^koordinate/letzte$',
        TemplateView.as_view(template_name='coordinate/finish.html'),
        name='finish'),
    url(r'^koordinate/(?P<lat>[0-9.]{1,36})/(?P<lon>[0-9.]{1,36})/(?P<question>\d+)$',
        coordinate.show,
        name='coordinate-show'),
    url(r'^koordinate/liste$',
        coordinate.CoordinateListView.as_view(),
        name='coordinate-list'),
    url(r'^koordinate/hinzufuegen$',
        coordinate.CoordinateAddView.as_view(),
        name='coordinate-add'),
    url(r'^koordinate/(?P<pk>\d+)/bearbeiten$',
        coordinate.CoordinateUpdateView.as_view(),
        name='coordinate-edit'),
    url(r'^koordinate/(?P<pk>\d+)/anzeigen$',
        coordinate.CoordinateDetaillView.as_view(),
        name='coordinate-detail'),
    url(r'^koordinate/(?P<pk>\d+)/loeschen$',
        coordinate.CoordinateDeleteView.as_view(),
        name='coordinate-delete'),

    # Questions
    url(r'^frage/liste$',
        question.QuestionListView.as_view(),
        name='question-list'),
    url(r'^frage/hinzufuegen$',
        question.QuestionAddView.as_view(),
        name='question-add'),
    url(r'^frage/(?P<pk>\d+)/bearbeiten$',
        question.QuestionUpdateView.as_view(),
        name='question-edit'),
    url(r'^frage/(?P<pk>\d+)/anzeigen$',
        question.QuestionDeatilView.as_view(),
        name='question-detail'),
    url(r'^frage/(?P<pk>\d+)/loeschen$',
        question.QuestionDeleteView.as_view(),
        name='question-delete'),

    # Answers
    url(r'^antwort/hinzufuegen$',
        answer.AnswerAddView.as_view(),
        name='answer-add'),
    url(r'^antwort/(?P<pk>\d+)/bearbeiten$',
        answer.AnswerUpdateView.as_view(),
        name='answer-edit'),
    url(r'^antwort/(?P<pk>\d+)/loeschen$',
        answer.AnswerDeleteView.as_view(),
        name='answer-delete'),

    # Answer configs
    url(r'^antwort-konfig/(?P<pk>\d+)/bearbeiten$',
        answer_config.AnswerConfigUpdateView.as_view(),
        name='answer-config-edit'),
    
    
    # Question configs
    url(r'^teamfrage/liste$',
        question_config.QuestionConfigListView.as_view(),
        name='question-config-list'),
    url(r'^teamfrage/liste/druckerfreundlich$',
        question_config.QuestionConfigListView.as_view(template_name='question_config/list_print.html'),
        name='question-config-list-printer'),
    url(r'^teamfrage/hinzufuegen$',
        question_config.QuestionConfigAddView.as_view(),
        name='question-config-add'),
    url(r'^teamfrage/(?P<pk>\d+)/anzeigen$',
        question_config.QuestionConfigDeatilView.as_view(),
        name='question-config-detail'),
    url(r'^teamfrage/(?P<pk>\d+)/loeschen$',
        question_config.QuestionConfigDeleteView.as_view(),
        name='question-config-delete'),

)
