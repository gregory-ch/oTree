from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Results(Page):
    def post(self):
        if self.participant.is_browser_bot:
            time.sleep(5)
        return super().post()


page_sequence = [Results]
