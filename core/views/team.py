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

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from utils.generic_views import WgerFormMixin
from utils.generic_views import WgerDeleteMixin
from utils.generic_views import WgerPermissionMixin

from core.models import Team


class TeamListView(WgerPermissionMixin, ListView):
    '''
    Overview of all available licenses
    '''
    model = Team
    permission_required = 'core.add_team'
    template_name = 'team/list.html'


class TeamAddView(WgerFormMixin, CreateView, WgerPermissionMixin):
    '''
    View to add a new team
    '''

    model = Team
    success_url = reverse_lazy('core:team-list')
    title = u'Team hinzufügen'
    form_action = reverse_lazy('core:team-add')
    permission_required = 'core.add_team'


class TeamUpdateView(WgerFormMixin, UpdateView, WgerPermissionMixin):
    '''
    View to update an existing team
    '''

    model = Team
    title = u'Team bearbeiten'
    success_url = reverse_lazy('core:team-list')
    permission_required = 'core.change_team'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(TeamUpdateView, self).get_context_data(**kwargs)
        context['form_action'] = reverse('core:team-edit', kwargs={'pk': self.object.id})
        context['title'] = _('Edit {0}'.format(self.object))
        return context


class TeamDeleteView(WgerDeleteMixin, DeleteView, WgerPermissionMixin):
    '''
    View to delete an existing team
    '''

    model = Team
    success_url = reverse_lazy('core:team-list')
    permission_required = 'core.delete_team'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(TeamDeleteView, self).get_context_data(**kwargs)
        context['title'] = _('Delete team {0}?'.format(self.object))
        context['form_action'] = reverse('core:team-delete', kwargs={'pk': self.kwargs['pk']})
        return context