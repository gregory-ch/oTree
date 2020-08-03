from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return  self.round_number == 1

class decision(Page):

    form_model = 'player'
    form_fields = ['hum_move']
    timeout_seconds = 45

    def before_next_page(self):
        self.player.randome_move_solver()
        self.player.comp_move_solver()
        self.player.result_solver()
        self.player.result_text_solver()
        self.player.comp_move_text_solver()
        self.player.cum_result_solver()
        self.player.set_cum_payoff()
        self.player.set_cum_payoff_comp()

    def vars_for_template(self):
        if self.round_number >=2:
            return {'a': self.round_number, 'cumulative_hum_payoff' : self.player.in_round(self.round_number - 1).cum_payoff_hum_second, 'cumulative_comp_payoff' : self.player.in_round(self.round_number - 1).cum_payoff_comp_second }
        else:
            return {'a': self.round_number,'cumulative_hum_payoff' : 0 , 'cumulative_comp_payoff' : 0}

class Results(Page):
    form_model = 'player'
    timeout_seconds = 45
    # def before_next_page(self):
    #     self.player.cum_result_solver()
    #     self.player.cum_result_solver_second()


    def vars_for_template(self):
        return {'a': self.round_number,'cumulative_hum_payoff' :  sum([p.cum_payoff_hum for p in self.player.in_all_rounds()])}

page_sequence = [
    Introduction,
    decision,
    Results
]
