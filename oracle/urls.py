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
from oracle.views import misc


urlpatterns = patterns('',

    # Index
    url(r'^dashboard$',
        misc.dashboard,
        name='dashboard'),

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
)