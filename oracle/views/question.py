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

from oracle.models import Question


class QuestionListView(WgerPermissionMixin, ListView):
    '''
    Overview of all available licenses
    '''
    model = Question
    permission_required = 'oracle.add_question'
    template_name = 'question/list.html'


class QuestionDeatilView(WgerPermissionMixin, DetailView):
    '''
    Deatail view for a question
    '''
    model = Question
    permission_required = 'oracle.add_question'
    template_name = 'question/detail.html'


class QuestionAddView(WgerFormMixin, CreateView, WgerPermissionMixin):
    '''
    View to add a new team
    '''

    model = Question
    success_url = reverse_lazy('oracle:question-list')
    title = u'Frage hinzufügen'
    form_action = reverse_lazy('oracle:question-add')
    permission_required = 'oracle.add_question'


class QuestionUpdateView(WgerFormMixin, UpdateView, WgerPermissionMixin):
    '''
    View to update an existing team
    '''

    model = Question
    title = u'Team bearbeiten'
    success_url = reverse_lazy('oracle:question-list')
    permission_required = 'oracle.change_question'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(QuestionUpdateView, self).get_context_data(**kwargs)
        context['form_action'] = reverse('oracle:question-edit', kwargs={'pk': self.object.id})
        context['title'] = _(u'Edit {0}'.format(self.object))
        return context


class QuestionDeleteView(WgerDeleteMixin, DeleteView, WgerPermissionMixin):
    '''
    View to delete an existing team
    '''

    model = Question
    success_url = reverse_lazy('oracle:question-list')
    permission_required = 'oracle.delete_question'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(QuestionDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Frage "{0}" löschen?'.format(self.object)
        context['form_action'] = reverse('oracle:question-delete', kwargs={'pk': self.kwargs['pk']})
        return context
