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

import uuid
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.views.generic import ListView, DetailView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from utils.generic_views import WgerFormMixin
from utils.generic_views import WgerDeleteMixin
from utils.generic_views import WgerPermissionMixin

from oracle.models import Coordinate


@login_required
def show(request, lat, lon, question):
    '''
    Small view that simply outputs two coordinates
    '''

    context = {'lat': lat,
               'lon': lon,
               'question': int(question)}
    return render(request, 'coordinate/show.html', context)


class CoordinateListView(WgerPermissionMixin, ListView):
    '''
    Overview of all available licenses
    '''
    model = Coordinate
    permission_required = 'oracle.add_coordinate'
    template_name = 'coordinate/list.html'


class CoordinateDetaillView(WgerPermissionMixin, DetailView):
    '''
    Deatail view for a question
    '''
    model = Coordinate
    permission_required = 'oracle.add_coordinate'
    template_name = 'coordinate/detail.html'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(CoordinateDetaillView, self).get_context_data(**kwargs)
        relative_url = reverse('oracle:check-step', kwargs={'uuid': self.object.uuid})
        context['qr_url'] = self.request.build_absolute_uri(relative_url)
        return context


class CoordinateAddView(WgerFormMixin, CreateView, WgerPermissionMixin):
    '''
    View to add a new team
    '''

    model = Coordinate
    success_url = reverse_lazy('oracle:coordinate-list')
    title = u'Frage hinzufügen'
    form_action = reverse_lazy('oracle:coordinate-add')
    permission_required = 'oracle.add_coordinate'

    def get_initial(self):
        return {'uuid': uuid.uuid4()}


class CoordinateUpdateView(WgerFormMixin, UpdateView, WgerPermissionMixin):
    '''
    View to update an existing team
    '''

    model = Coordinate
    title = u'Team bearbeiten'
    success_url = reverse_lazy('oracle:coordinate-list')
    permission_required = 'oracle.change_coordinate'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(CoordinateUpdateView, self).get_context_data(**kwargs)
        context['form_action'] = reverse('oracle:coordinate-edit', kwargs={'pk': self.object.id})
        context['title'] = _(u'Edit {0}'.format(self.object))
        return context


class CoordinateDeleteView(WgerDeleteMixin, DeleteView, WgerPermissionMixin):
    '''
    View to delete an existing team
    '''

    model = Coordinate
    success_url = reverse_lazy('oracle:coordinate-list')
    permission_required = 'oracle.delete_coordinate'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(CoordinateDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Koordinate "{0}" löschen?'.format(self.object)
        context['form_action'] = reverse('oracle:coordinate-delete', kwargs={'pk': self.kwargs['pk']})
        return context