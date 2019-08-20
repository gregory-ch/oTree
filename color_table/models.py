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
    name_in_url = 'color_table'
    players_per_group = None
    num_rounds = 1
    delta = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    x = models.IntegerField()
    num_square = models.IntegerField()
    y =  models.PositiveIntegerField(
        verbose_name='''введите уровень риска (от 1 до 8, где 8 минимальный риск)''',
        choices=[1, 2, 3, 4, 5, 6, 7, 8,],
        widget=widgets.RadioSelectHorizontal()
    )
    # q = models.IntegerField()

    def random_item(self):
        self.x = random.randint(140, 240)

    def count_num_square(self):
        self.num_square = random.randint(1, 16)
    #
    # def count_y(self):
    #     self.y = [k * 5 for k in self.z]
    #     self.y.insert(random.randrange(0, 15), 0)
    #
    # def count_q(self):
    #     self.q = [i + x for i in self.y]
