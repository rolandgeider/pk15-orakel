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


from oracle.models import TeamAnswerLog
from oracle.models import QuestionConfig
from oracle.models import Coordinate
from oracle.models import AnswerConfig


def next_coordinates(team):
    '''
    returns the next coordinates for this team
    '''

    #
    # First coordinate
    #
    if not TeamAnswerLog.objects.filter(team=team).count():
        return QuestionConfig.objects.filter(team=team).first().coordinate

    #
    # During the game
    #
    answer_log = TeamAnswerLog.objects.filter(team=team).last()

    # last answer was wrong, send the team to the jail
    if answer_log.team_answer.is_wrong:
        return Coordinate.objects.filter(is_jail=True).first()

    # Answer was correct, look up next step
    answer_config = AnswerConfig.objects.get(answer=answer_log.team_answer,
                                             question_config=answer_log.question_config)
    return answer_config.next_coordinate
