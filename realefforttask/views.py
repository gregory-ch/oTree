from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class ChoosingDiff(Page):
    form_model = models.Player
    form_fields = ['difficulty']
    timeout_submission = {'difficulty': 5}

    def vars_for_template(self):
        frm = self.get_form()
        f = frm['difficulty']

        return {'data': zip(Constants.diff_choices, f)}


class WorkPage(Page):
    # form_model = models.Player
    # form_fields = ['tasks_dump']

    timer_text = 'Time left to complete this round:'
    timeout_seconds = Constants.task_time

    def is_displayed(self) -> bool:
        return self.player.tasks.filter(answer__isnull=False).count() < 1

    def vars_for_template(self):
        return {"task": self.player.get_task()}

    def before_next_page(self):
        self.player.dump_tasks()
        self.player.set_payoff()


class Results(Page):
    ...


page_sequence = [
    ChoosingDiff,
    WorkPage,
    Results,
]
