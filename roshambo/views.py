from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants



class decision(Page):

    form_model = 'group'
    form_fields = ['hum_move']




class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.randome_move_solver()
        self.group.comp_move_solver()
        self.group.comp_move_text_solver()
        self.group.result_solver()
        self.group.result_text_solver()



class Results(Page):
    form_model = 'group'


page_sequence = [
    decision,
    ResultsWaitPage,
    Results
]
