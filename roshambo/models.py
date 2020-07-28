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
    name_in_url = 'roshambo'
    players_per_group = None
    num_rounds = 10
    beta = 0.2

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    hum_move = models.IntegerField(
        label='Ваш выбор:',
            choices=[
                [0, 'Камень'],
                [1, 'Бумага'],
                [2, 'Ножницы'],
            ]
        )
    comp_move = models.IntegerField(min=0, max=2)
    comp_move_text =  models.StringField()
    result = models.IntegerField(min=0, max=2)
    randome_move = models.FloatField()
    result_text = models.StringField()

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
                self.comp_move = int((self.in_round(self.round_number - 1).hum_move + self.in_round(self.round_number - 1).result)%3)
            else:
                self.comp_move = random.randint(0, 2)
        else:
            self.comp_move = random.randint(0, 2)

# player for Hum move
#  self.comp_move = self.in_round(self.round_number - 1).hum_move
class Player(BasePlayer):
    pass