from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['age',
                   'gender',
                   'height',
                   'city',
                   'univ',
                   'satis',
                   'trust',
                   'guess',
                   'math',
                   'tigr',
                   "trend0",
                   'trend2',
                   'equi']


    # def before_next_page(self):
    #         self.player.set_payoff()

page_sequence = [
    MyPage
    ]
