from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'roshambo_single'
    players_per_group = None
    num_rounds = 10
    beta = 0.2

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    hum_move = models.IntegerField(
        choices=[
            [0, 'Камень'],
            [1, 'Бумага'],
            [2, 'Ножницы'],

        ],
        widget=widgets.RadioSelectHorizontal
    )
    comp_move = models.IntegerField(min=0, max=2)
    result = models.IntegerField(min=0, max=2)
    randome_move = models.FloatField()
    result_text = models.StringField()
    comp_move_text = models.StringField()
    cum_payoff_hum = models.FloatField()
    cum_payoff_comp = models.FloatField()
    cum_payoff_hum_second = models.FloatField()
    cum_payoff_comp_second = models.FloatField()

    def randome_move_solver(self):
        self.randome_move = random.uniform(0, 1)

        # for result 0 = tie 2 = win 1 = loose

    def result_solver(self):
        if self.hum_move == self.comp_move:
            self.result = 0
        elif (self.hum_move == 0 and self.comp_move == 2) or (self.hum_move == 1 and self.comp_move == 0) or (
                        self.hum_move == 2 and self.comp_move == 1):
            self.result = 2
        else:
            self.result = 1

    def cum_result_solver(self):
        if self.hum_move == self.comp_move:
            self.cum_payoff_hum = 0
            self.cum_payoff_comp = 0
        elif (self.hum_move == 0 and self.comp_move == 2) or (self.hum_move == 1 and self.comp_move == 0) or (
                        self.hum_move == 2 and self.comp_move == 1):
            self.cum_payoff_hum = 1
            self.cum_payoff_comp = 0
        else:
            self.cum_payoff_comp = 1
            self.cum_payoff_hum = 0

    # def cum_result_solver_second(self):
    #     self.cum_payoff_hum_second = sum(self.in_all_rounds.cum_payoff_hum)
    #     self.cum_payoff_comp_second = sum(self.in_all_rounds.cum_payoff_hum)

    def set_cum_payoff(self):
        cum_payoff = 0
        for i in range(self.round_number):
            cum_payoff += self.in_round(i+1).cum_payoff_hum
        self.cum_payoff_hum_second = cum_payoff

    def set_cum_payoff_comp(self):
        cum_payoff = 0
        for i in range(self.round_number):
            cum_payoff += self.in_round(i+1).cum_payoff_comp
        self.cum_payoff_comp_second = cum_payoff

    def result_text_solver(self):
        if self.result == 0:
            self.result_text = 'сыграли в ничью'
        elif self.result == 2:
            self.result_text = 'выиграли'
        else:
            self.result_text = 'проиграли'

    def comp_move_text_solver(self):
        if self.comp_move == 0:
            self.comp_move_text = 'камень'
        elif self.comp_move == 1:
            self.comp_move_text = 'бумага'
        else:
            self.comp_move_text = 'ножницы'

    def comp_move_solver(self):
        if self.round_number >= 2:
            if self.randome_move >= Constants.beta:
                # for pl in self.get_players():
                #     (pl.in_round(self.round_number - 1).hum_move + 2)%3
                self.comp_move = (self.in_round(self.round_number - 1).comp_move + self.in_round(self.round_number - 1).result) % 3
            else:
                self.comp_move = random.randint(0, 2)
        else:
            self.comp_move = random.randint(0, 2)

            # player for Hum move
            #  self.comp_move = self.in_round(self.round_number - 1).hum_move
