"""
Él hizo esto. No debe de cambiarse si no se quiere:

from otree.api import {
    BaseConstants,
    BaseGroups,
    BasePlayer,
    BaseSubsession,
    Page,
    WaitPage
}
"""
from otree.api import *


doc = """
A simple Tullock contest game with possible different 
"""


class C(BaseConstants):
    NAME_IN_URL = 'contest'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class SubSession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Intro(Page):
    pass


class SetupRound(WaitPage):
    pass


class Decision(Page):
    pass

class WaitForDesicions(WaitPage):
    pass

class Results(Page):
    pass

class EndBlock(Page):
    pass

page_sequence = [
    Intro,
    SetupRound,
    Decision,
    WaitForDesicions,
    Results,
    EndBlock,
]
#It let you to have the coma at the end