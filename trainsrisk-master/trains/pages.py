from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class DifficultyChoice(Page):
    form_model = 'player'
    form_fields = ['difficulty']


class Task(Page):
    form_model = 'player'
    form_fields = ['task']


class Results(Page):
    pass


page_sequence = [
    DifficultyChoice,
    Task,
    Results
]
