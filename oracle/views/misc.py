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
import random

from django.conf import settings
from django import forms
from django.contrib.auth.decorators import login_required
from django.core import mail
from django.core.urlresolvers import reverse
from django.forms import Form
from django.forms import Textarea
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from oracle.helpers import next_coordinates

from oracle.models import Coordinate
from oracle.models import QuestionConfig
from oracle.models import AnswerConfig
from oracle.models import Answer
from oracle.models import TeamAnswerLog


@login_required
def dashboard(request):
    '''
    Show the index page
    '''
    next_coordinate = None if request.user.has_perm('oracle.add_question') \
        else next_coordinates(request.user.userprofile.team)
    context = {'coord': next_coordinate}
    return render(request, 'index.html', context)


@login_required
def check_step(request, uuid):
    '''

    :param request:
    :param uuid:
    :return:
    '''
    context = {}
    coordinate = get_object_or_404(Coordinate, uuid=uuid)
    context['coordinate'] = coordinate
    team = request.user.userprofile.team

    # Check if the user was sent to jail
    #
    # In this case, the next coordinate is the first correct answer of
    # the previous question and there is no need to answer anything.
    if coordinate.is_jail:
        answer_log = TeamAnswerLog.objects.filter(team=team).last()
        answer_config_set = answer_log.question_config.answerconfig_set
        next_coordinate = answer_config_set.filter(answer__is_wrong=False).first().next_coordinate
        return HttpResponseRedirect(reverse('oracle:coordinate-show',
                                            kwargs={'lat': next_coordinate.lat,
                                                    'lon': next_coordinate.lon,
                                                    'question': 100}))

    if request.user.has_perm('oracle.add_question'):
        return HttpResponseForbidden('Sorry admin, only regular users can access this')

    question_config = get_object_or_404(QuestionConfig,
                                        coordinate=coordinate,
                                        team=team)

    context['question_config'] = question_config

    #
    # Check that the user allowed to access this step
    #

    # Is it the first step (there are no answers pointing to it)?
    if AnswerConfig.objects.filter(next_coordinate=coordinate).count():
        pass

    # Is it the correct step?
    pass

    # Answer form, defined here because it's easier to set the queryset and
    # is used only once anyway
    class AnswerLogForm(Form):
        answer = forms.ModelChoiceField(queryset=Answer.objects.filter(question=question_config.question),
                                        empty_label=None,
                                        widget=forms.RadioSelect,
                                        label=u"Antwort")

        place = forms.CharField(label=u"Wo sind wir?",
                                required=False)
        reference = forms.CharField(label=u"Bezug zur Intevation",
                                    widget=Textarea({'cols': 40, 'rows': 3}),
                                    required=False)

    form = AnswerLogForm()
    if request.method == 'POST':
        form = AnswerLogForm(data=request.POST)

        if form.is_valid():

            # Check if the team already answered this question and notify the
            # santa task force that they have been naughty
            if TeamAnswerLog.objects.filter(team=team, question_config=question_config).exists():

                subject = 'Team {} hat geschummelt!'.format(team)
                context = {'question_config': question_config,
                           'team': team,
                           'answer': form.cleaned_data['answer'],
                           'place': form.cleaned_data['place'],
                           'reference': form.cleaned_data['reference']}
                message = render_to_string('user/email_double_answer.html', context)
                mail.send_mail(subject,
                               message,
                               settings.EMAIL_FROM,
                               settings.EMAIL_PENALTY,
                               fail_silently=False)
                return HttpResponseRedirect(reverse('oracle:dashboard'))

            answer_log = TeamAnswerLog()
            answer_log.team = team
            answer_log.question_config = question_config
            answer_log.team_answer = form.cleaned_data['answer']
            answer_log.place = form.cleaned_data['place']
            answer_log.reference = form.cleaned_data['reference']
            answer_log.save()

            # If this is the last question, don't redirect to dashboard
            if not next_coordinates(request.user.userprofile.team):
                return HttpResponseRedirect(reverse('oracle:finish'))
            else:
                return HttpResponseRedirect(reverse('oracle:dashboard'))
        else:
            pass

    context['form'] = form
    return render(request, 'check_step.html', context)
