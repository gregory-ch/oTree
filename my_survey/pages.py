from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age',
                   'height',
                   'gender',
                   'state',
                   'education',
                   'wage',
                   'experience',
                   'mark',
                   'loneliness',
                   'trust',
                   'feedback_1',
                   'feedback_2',
                   'feedback_3'
                   ]

    # def age_error_message(self, value):
    #     print('value is', value)
    #     if value  != 22:
    #         return ''

    # def before_next_page(self):
    #     self.player.age_error_message()

class Block_2(Page):
    form_model = 'player'
    form_fields = [ 'max_satisf_min_1',
                    'max_satisf_min_2',
                    'max_satisf_min_3',
                    'max_satisf_min_4',
                    'max_satisf_min_5',
                    'max_satisf_min_6',
                    'max_satisf_min_7',
                    'max_satisf_min_8',
                    'max_satisf_min_9',
                    'max_satisf_min_10',
                    'max_satisf_min_11',
                    'max_satisf_min_12',
                    'max_satisf_min_13',
                    'max_satisf_min_14',
                    'max_satisf_min_15',
                    'max_satisf_min_16',
                    'max_satisf_min_17',
                    'max_satisf_min_18',
                    'max_satisf_min_19',
                    'max_satisf_min_20',
                    ]

page_sequence = [
    Demographics,
    Block_2,
]
