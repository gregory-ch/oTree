from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)

        if self.round_number == 1:
            yield (pages.quiz,
                   {'task_1': 40   ,
                    'task_2': 0.6  ,
                    'task_3': 0.4  ,
                    'task_4': 7    ,
                    'task_5': 437.5,
                    'task_6': 4    ,
                    })
        if self.player.role() == 'principal':
            yield (pages.Offer,
                   {'agent_fixed_pay': 5,
                   'agent_piece_rate': 2
                    })

        if self.player.role() == 'agent':
            yield (pages.Accept,
                   {'Hum_effort': 5,
                    })

        yield (pages.Results)