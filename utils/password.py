# -*- coding: utf-8 -*-

# This file is part of AISE industry classification network.
#
# AISE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AISE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License

import string
import random


def password_generator(size=12,
                       chars=string.ascii_uppercase.replace('L', '').replace('O', '')
                             + string.ascii_lowercase.replace('l', '')
                             + string.digits.replace('1', '',).replace('0', '')):
    '''
    Very simple password generator.
    '''
    return ''.join(random.choice(chars) for x in range(size))
