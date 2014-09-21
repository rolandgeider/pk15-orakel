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
from django.views.generic import UpdateView

from utils.generic_views import WgerFormMixin
from utils.generic_views import WgerPermissionMixin
from oracle.models import AnswerConfig


class AnswerConfigUpdateView(WgerFormMixin, UpdateView, WgerPermissionMixin):
    '''
    View to update an existing answer config
    '''

    model = AnswerConfig
    title = u'Teamantwort bearbeiten'
    success_url = reverse_lazy('oracle:answer-config-list')
    permission_required = 'oracle.change_answerconfig'

    def get_success_url(self):
        return reverse('oracle:question-config-detail', kwargs={'pk': self.object.question_config.pk})

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(AnswerConfigUpdateView, self).get_context_data(**kwargs)
        context['form_action'] = reverse('oracle:answer-config-edit', kwargs={'pk': self.object.id})
        context['title'] = _('Edit {0}'.format(self.object))
        return context
