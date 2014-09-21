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

from oracle.models import QuestionConfig
from oracle.models import AnswerConfig


class QuestionConfigListView(WgerPermissionMixin, ListView):
    '''
    Overview of all available licenses
    '''
    model = QuestionConfig
    permission_required = 'oracle.add_questionconfig'
    template_name = 'question_config/list.html'


class QuestionConfigDeatilView(WgerPermissionMixin, DetailView):
    '''
    Deatail view for a question
    '''
    model = QuestionConfig
    permission_required = 'oracle.add_questionconfig'
    template_name = 'question_config/detail.html'

class QuestionConfigAddView(WgerFormMixin, CreateView, WgerPermissionMixin):
    '''
    View to add a new team
    '''

    model = QuestionConfig
    success_url = reverse_lazy('oracle:question-config-list')
    title = u'Frage hinzufügen'
    form_action = reverse_lazy('oracle:question-config-add')
    permission_required = 'oracle.add_questionconfig'

    def get_initial(self):
        return {'uuid': uuid.uuid4()}

    def form_valid(self, form):
        '''
        Create answer configs for each answer the question has
        '''
        question_config = form.save()

        for answer in form.instance.question.answer_set.all():
            answer_config = AnswerConfig()
            answer_config.answer = answer
            answer_config.question_config = question_config
            answer_config.save()

        return super(QuestionConfigAddView, self).form_valid(form)


class QuestionConfigUpdateView(WgerFormMixin, UpdateView, WgerPermissionMixin):
    '''
    View to update an existing team
    '''

    model = QuestionConfig
    title = u'Team bearbeiten'
    success_url = reverse_lazy('oracle:question-config-list')
    permission_required = 'oracle.change_question'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(QuestionConfigUpdateView, self).get_context_data(**kwargs)
        context['form_action'] = reverse('oracle:question-config-edit', kwargs={'pk': self.object.id})
        context['title'] = _('Edit {0}'.format(self.object))
        return context


class QuestionConfigDeleteView(WgerDeleteMixin, DeleteView, WgerPermissionMixin):
    '''
    View to delete an existing team
    '''

    model = QuestionConfig
    success_url = reverse_lazy('oracle:question-config-list')
    permission_required = 'oracle.delete_question'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(QuestionConfigDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Frage "{0}" löschen?'.format(self.object)
        context['form_action'] = reverse('oracle:question-config-delete', kwargs={'pk': self.kwargs['pk']})
        return context