# from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class IntroductionWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.risk_counter()

class Introduction(Page):
    def is_displayed(self):
        return  self.round_number == 1

class quiz (Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['task_1', 'task_2','task_3','task_4','task_5','task_6',]

    def task_1_error_message(self, value):
        print('value is', value)
        if value  != '40':
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей' \
                   'попытки ввода неверного значения'

    def task_2_error_message(self, value):
        print('value is', value)
        if value  != '0.6':
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей' \
                   'попытки ввода неверного значения'


    def task_3_error_message(self, value):
        print('value is', value)
        if value  != '0.4':
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей' \
                   'попытки ввода неверного значения'

    def task_4_error_message(self, value):
        print('value is', value)
        if value != '7':
            self.player.numb_errors += 1
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей' \
                   'попытки ввода неверного значения'

    def task_5_error_message(self, value):
        print('value is', value)
        if value != '437.5':
            self.player.numb_errors += 1
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей' \
                   'попытки ввода неверного значения'

    def task_6_error_message(self, value):
        print('value is', value)
        if value != 4:
            self.player.numb_errors += 1
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей' \
                   'попытки ввода неверного значения'


class Offer(Page):
    def is_displayed(self):
        return self.player.role() == 'principal'

    form_model = 'group'
    form_fields = ['agent_fixed_pay', 'agent_piece_rate']



class OfferWaitPage(WaitPage):
    def vars_for_template(self):
        if self.player.role() == 'agent':
            body_text = "Вы Участник 2, ожидайте пока Участник 1 предложит вам контракт."
        else:
            body_text = "Ожидайте Участника 2."
        return {'body_text': body_text}

    def after_all_players_arrive(self):
        self.group.randome_move_solver()
        self.group.robot_moves_principal()


class Accept(Page):
    def is_displayed(self):
        return self.player.role() == 'agent'

    form_model = 'group'
    form_fields = ['Hum_effort']



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()
        self.group.x_counter_H()
        self.group.x_counter_R()



class Results(Page):
    pass





page_sequence = [IntroductionWaitPage,
                 Introduction,
                 quiz,
                 Offer,
                 OfferWaitPage,
                 Accept,
                 ResultsWaitPage,
                 Results]

