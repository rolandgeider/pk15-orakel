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

import logging

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.utils import translation
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as Django_User
from django.contrib.auth.views import login as django_loginview
from django.contrib import messages

#from wger.core.models import Language
#from wger.utils.constants import USER_TAB
#from wger.core.forms import RegistrationFormNoCaptcha

logger = logging.getLogger('wger.custom')


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
    Logout the user. For temporary users, delete them.
    '''
    user = request.user
    django_logout(request)
    return HttpResponseRedirect(reverse('core:login'))
