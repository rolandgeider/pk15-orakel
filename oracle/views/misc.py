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
from django import forms

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms import ModelForm, RadioSelect, Form, Textarea
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from oracle.models import Coordinate, QuestionConfig, AnswerConfig, Answer, TeamAnswerLog


@login_required
def dashboard(request):
    '''
    Show the index page with the current active question
    '''

    context = {}
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

    # Is it "jail"?

    class AnswerLogForm(Form):
        answer = forms.ModelChoiceField(queryset=Answer.objects.filter(question=question_config.question),
                                        empty_label=u"--- bitte wählen ---",
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
            answer_log = TeamAnswerLog()
            answer_log.team = team
            answer_log.question_config = question_config
            answer_log.team_answer = form.cleaned_data['answer']
            answer_log.place = form.cleaned_data['place']
            answer_log.reference = form.cleaned_data['reference']
            answer_log.save()

            answer_config = AnswerConfig.objects.get(answer=form.cleaned_data['answer'],
                                                     question_config__team=request.user.userprofile.team)
            coordinate = answer_config.next_coordinate

            #print(coordinate)
            return HttpResponseRedirect(reverse('oracle:coordinate-show',
                                                kwargs={'lat': coordinate.lat,
                                                        'lon': coordinate.lon}))
        else:
            pass

    context['form'] = form

    #return HttpResponseRedirect(reverse('oracle:dashboard'))
    #print question_config
    return render(request, 'check_step.html', context)