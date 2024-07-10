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
    NUM_ROUNDS = 2
    ENDOWMENT = 20
    COST_PER_TICKET = 1

class Subsession(BaseSubsession):
    is_paid = models.BooleanField()

    def setup(self):
        #print("hello word from setup")
        self.is_paid = (self.round_number == 1)

#Subsession is a round!!!

class Group(BaseGroup):
    def setup(self):
        for player in self.get_players():
            player.setup()


class Player(BasePlayer):
    endowment = models.StringField()
    cost_ticket = models.IntegerField()
    tickets_purchased = models.IntegerField()
    is_winner = models.BooleanField()
    #is_paid = models.BooleanField()
    earnings = models.IntegerField()

    def setup(self):
        self.endowment = C.ENDOWMENT
        self.cost_per_ticket = C.COST_PER_TICKET


#We define a session.
#def creating_session(subsession):
#    subsession.setup()

# PAGES
class Intro(Page):
    pass


class SetupRound(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def afeter_all_players_arrive(subsession):
        subsession.setup()


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