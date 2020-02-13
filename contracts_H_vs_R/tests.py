from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)

        if self.round_number == 1:
            yield (pages.question,
                   {
                    'social_media_time_spend':2,
                    'numb_of_last_books': 3
                    })

        if self.round_number == 1:
            yield (pages.quiz,
                   {'task_1': 40   ,
                    'task_2': 15 ,
                    'task_3': 0.4  ,
                    'task_4': 7    ,
                    'task_5': 470,
                    'task_6': 4   ,

                    })
        if self.player.role() == 'principal':
            yield (pages.Offer,
                   {'viewed_risk_preff': 1,
                    'viewed_social_media_time_spend': 1,
                    'viewed_numb_of_last_books': 1,
                    'agent_fixed_pay': 5,
                   'agent_piece_rate': 2,
                    'expected_efforts': 2
                    })

        if self.player.role() == 'agent':
            yield (pages.Accept,
                   {'Hum_effort': 5,
                    })

        yield (pages.Results)