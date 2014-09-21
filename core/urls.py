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

from core.views import user
from core.views import team


urlpatterns = patterns('',

    # The landing page
    url(r'^$',
        user.index,
        name='index'),

    
    # User
    #url(r'^$',
    url(r'^user/login$',
        user.login,
        name='login'),

    # Teams
    url(r'^team/(?P<pk>\d+)/list$',
        team.TeamDetailView.as_view(),
        name='team-detail'),
    url(r'^team/list$',
        team.TeamListView.as_view(),
        name='team-list'),
    url(r'^team/add$',
        team.TeamAddView.as_view(),
        name='team-add'),
    url(r'^team/(?P<pk>\d+)/edit',
        team.TeamUpdateView.as_view(),
        name='team-edit'),
    url(r'^team/(?P<pk>\d+)/delete',
        team.TeamDeleteView.as_view(),
        name='team-delete'),
)