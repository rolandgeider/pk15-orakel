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
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

logger = logging.getLogger('wger.custom')


def index(request):
    '''
    Index page
    '''
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('oracle:dashboard'))
    else:
        return HttpResponseRedirect(reverse('core:login'))


def login(request):
    '''
    Small wrapper around the django login view
    '''

    context = {}
    if request.REQUEST.get('next'):
        context['next'] = request.REQUEST.get('next')

    # Sane login, with POST
    if request.method == "POST":
        return django_loginview(request,
                            template_name='user/login.html',
                            extra_context=context)
        
    # log in with GET parameters so users can easily get in by scanning a QR code
    elif request.REQUEST.get('get_login'):
        
        form = AuthenticationForm(request, data=request.GET)
        if form.is_valid():

            auth_login(request, form.get_user())
            return HttpResponseRedirect(reverse('oracle:dashboard'))

        
    return django_loginview(request,
                            template_name='user/login.html',
                            extra_context=context)



def logout(request):
    '''
    Logout the user.
    '''
    django_logout(request)
    return HttpResponseRedirect(reverse('core:login'))
