# from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from decimal import Decimal



class PreWaitPage(WaitPage):
    def is_displayed(self):
        return  self.round_number == 1
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.avarege_risk_counter()

class IntroductionWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.risk_counter()
        self.group.set_swicher()

class Introduction(Page):
    def is_displayed(self):
        return  self.round_number == 1

class quiz (Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['task_1', 'task_2','task_3','task_4','task_5','task_6','social_media_time_spend', 'numb_of_last_books']

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
            self.player.numb_errors = 1
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей' \
                   'попытки ввода неверного значения'

    def task_5_error_message(self, value):
        print('value is', value)
        if value != '437.5':
            self.player.numb_errors = 1
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей' \
                   'попытки ввода неверного значения'

    def task_6_error_message(self, value):
        print('value is', value)
        if value != 4:
            self.player.numb_errors = 1
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей' \
                   'попытки ввода неверного значения'


class Offer(Page):
    def is_displayed(self):
        return self.player.role() == 'principal'

    form_model = 'group'
    form_fields = ['viewed_risk_preff','viewed_social_media_time_spend','viewed_numb_of_last_books',
                   'agent_fixed_pay','expected_efforts',  'agent_piece_rate']

    def error_message(self, values):
        print('Сумма введенных значений', values)
        if float(values['agent_fixed_pay']) + values['agent_piece_rate']*values['expected_efforts']  > 100:
            return 'Сумма переменной и постоянной выплат не должна превышать 100'



class OfferWaitPage(WaitPage):
    def vars_for_template(self):
        if self.player.role() == 'agent':
            body_text = "Вы Участник 2, ожидайте пока Участник 1 предложит вам контракт."
        else:
            body_text = "Ожидайте Участника 2."
        return {'body_text': body_text}

    def after_all_players_arrive(self):
        self.group.randome_move_solver()
        if Constants.session_swicher != 1:
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
        if Constants.session_swicher != 1:
            self.group.x_counter_R()
        self.group.final_payoff()






class Results(Page):



    def vars_for_template(self):
        if self.round_number == Constants.num_rounds:
             a = []
             b = []
             for i in range(1, Constants.num_rounds+1):
                 a.append(i)
                 b.append(self.player.in_round(i).payoff)

             return {'payset': zip(a, b,)}

    pass





page_sequence = [PreWaitPage,
                 IntroductionWaitPage,
                 Introduction,
                 quiz,
                 Offer,
                 OfferWaitPage,
                 Accept,
                 ResultsWaitPage,
                 Results]

