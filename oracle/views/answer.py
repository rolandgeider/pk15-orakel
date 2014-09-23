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
from django.views.generic import ListView, DetailView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from utils.generic_views import WgerFormMixin
from utils.generic_views import WgerDeleteMixin
from utils.generic_views import WgerPermissionMixin

from oracle.models import Answer


class AnswerAddView(WgerFormMixin, CreateView, WgerPermissionMixin):
    '''
    View to add a new team
    '''

    model = Answer
    #success_url = reverse_lazy('oracle:answer-list')
    title = u'Antwort hinzufügen'
    form_action = reverse_lazy('oracle:answer-add')
    permission_required = 'oracle.add_answer'

    def get_success_url(self):
        return reverse('oracle:question-detail', kwargs={'pk': self.object.question.pk})

    def get_initial(self):
        return {'question': self.request.GET.get('question', '')}


class AnswerUpdateView(WgerFormMixin, UpdateView, WgerPermissionMixin):
    '''
    View to update an existing answer
    '''

    model = Answer
    title = u'Antwort bearbeiten'
    permission_required = 'oracle.change_answer'

    def get_success_url(self):
        return reverse('oracle:question-detail', kwargs={'pk': self.object.question.pk})

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(AnswerUpdateView, self).get_context_data(**kwargs)
        context['form_action'] = reverse('oracle:answer-edit', kwargs={'pk': self.object.id})
        context['title'] = u'Bearbeite {0}'.format(self.object)
        return context


class AnswerDeleteView(WgerDeleteMixin, DeleteView, WgerPermissionMixin):
    '''
    View to delete an existing answer
    '''

    model = Answer
    success_url = reverse_lazy('oracle:answer-list')
    permission_required = 'oracle.delete_answer'

    def get_success_url(self):
        return reverse('oracle:question-detail', kwargs={'pk': self.object.question.pk})

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(AnswerDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Antwort "{0}" löschen?'.format(self.object)
        context['form_action'] = reverse('oracle:answer-delete', kwargs={'pk': self.kwargs['pk']})
        return context