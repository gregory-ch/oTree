from otree.api import Currency as c, currency_range

from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):

    def play_round(self):

        yield (pages.Demographics, {
            'age': 24,
            'gender': 'Male',
            'height': 166,
            'gender': 'Мужской',
            'state': 0,
            'education': 'Диплом бакалавра',
            'wage': 20000,
            'experience':'Нет',
            'mark': 75,
            'loneliness': 'Почти никогда',
            'trust':'Большинству людей можно доверять',
            'feedback_1': 0,
            'feedback_2': 0,
            'feedback_3': 0,
            'feedback_4': 0

            })

        yield (pages.Block_2, {
            'max_satisf_min_1': 3,
            'max_satisf_min_2': 3,
            'max_satisf_min_3': 3,
            'max_satisf_min_4': 3,
            'max_satisf_min_5': 3,
            'max_satisf_min_6': 3,
            'max_satisf_min_7': 3,
            'max_satisf_min_8': 3,
            'max_satisf_min_9': 3,
            'max_satisf_min_10':3,
            'max_satisf_min_11':3,
            'max_satisf_min_12':3,
            'max_satisf_min_13':3,
            'max_satisf_min_14':3,
            'max_satisf_min_15':3,
            'max_satisf_min_16':3,
            'max_satisf_min_17':3,
            'max_satisf_min_18':3,
            'max_satisf_min_19':3,
            'max_satisf_min_20':3,
        })

