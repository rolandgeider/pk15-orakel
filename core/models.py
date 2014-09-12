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


from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    '''
    Model for a team
    '''
    name = models.CharField(verbose_name=u'Name',
                            max_length=30)

    def get_owner_object(self):
        '''
        Needed for generic views, not used
        '''
        return None

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    '''
    User profile
    '''

    user = models.OneToOneField(User,
                                editable=False)

    team = models.ForeignKey(Team)
    '''
    Team this user belongs to
    '''
