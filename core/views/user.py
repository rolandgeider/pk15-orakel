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

import logging

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as django_logout
from django.contrib.auth.views import login as django_loginview


logger = logging.getLogger('wger.custom')


def index(request):
    '''
    Index page
    '''
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('core:dashboard'))
    else:
        return HttpResponseRedirect(reverse('core:login'))


def login(request):
    '''
    Small wrapper around the django login view
    '''

    context = {}
    if request.REQUEST.get('next'):
        context['next'] = request.REQUEST.get('next')

    return django_loginview(request,
                            template_name='user/login.html',
                            extra_context=context)



def logout(request):
    '''
    Logout the user.
    '''
    django_logout(request)
    return HttpResponseRedirect(reverse('core:login'))
