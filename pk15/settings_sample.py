# -*- coding: utf-8 -*-
# This file is part of PK15 Orakel
#
# PK15 Orakel is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PK15 Orakel is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

from pk15.settings_global import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''


# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FROM = 'Your Name <your.email@example.com>'
EMAIL_PENALTY = ['your.email@example.com',]