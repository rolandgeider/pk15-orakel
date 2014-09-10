# -*- coding: utf-8 -*-

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License


from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth import views
from django.core.urlresolvers import reverse_lazy

from core.views import user
#from wger.core.views import misc
#from wger.core.views import license


urlpatterns = patterns('',

    # The landing page
    #url(r'^$',
    #    misc.index,
    #    name='index'),

    
    # User
    url(r'^$',
        user.login,
        name='login'),
    
)

# Password reset is implemented by Django, no need to cook our own soup here
# (besides the templates)
urlpatterns = urlpatterns + patterns('',
    #url(r'^user/login$',
    #    user.login,
    #    name='login'),

    url(r'^user/password/change$',
        views.password_change,
        {'template_name': 'user/change_password.html',
          'post_change_redirect': reverse_lazy('core:preferences')},
        name='change-password'),

    url(r'^user/password/reset/$',
        views.password_reset,
        {'template_name': 'user/password_reset_form.html',
         'email_template_name': 'user/password_reset_email.html',
         'post_reset_redirect': reverse_lazy('core:password_reset_done')},
        name='password_reset'),

    url(r'^user/password/reset/done/$',
        views.password_reset_done,
        {'template_name': 'user/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^user/password/reset/check/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$',
        views.password_reset_confirm,
        {'template_name': 'user/password_reset_confirm.html',
         'post_reset_redirect': reverse_lazy('core:password_reset_complete')},
        name='password_reset_confirm'),

    url(r'^user/password/reset/complete/$',
        views.password_reset_complete,
        {'template_name': 'user/password_reset_complete.html'},
        name='password_reset_complete'),
)
