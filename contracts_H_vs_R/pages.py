# from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from decimal import Decimal



class PreWaitPage(WaitPage):
    # def is_displayed(self):
    #     return  self.round_number == 1
    wait_for_all_groups = True


    def vars_for_template(self):
        body_text = "Ожидайте пока другие участники дойдут до этапа 2"
        return {'body_text': body_text}

    def after_all_players_arrive(self):
        self.subsession.avarege_risk_counter()

class IntroductionWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.risk_counter()
        self.group.set_swicher()


class question(Page):
    def is_displayed(self):
        return  self.round_number == 1
    form_model = 'player'
    form_fields = ['social_media_time_spend', 'numb_of_last_books']

class Introduction(Page):
    def is_displayed(self):
        return  self.round_number == 1



class quiz (Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['task_1', 'task_2','task_4','task_5','task_6',]

    def task_1_error_message(self, value):
        print('value is', value)
        if value  != '55':
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей ' \
                   'попытки ввода неверного значения'

    def task_2_error_message(self, value):
        print('value is', value)
        if value  != '25':
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей ' \
                   'попытки ввода неверного значения'



    def task_4_error_message(self, value):
        print('value is', value)
        if value != '7':
            self.player.numb_errors = 1
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей ' \
                   'попытки ввода неверного значения'

    def task_5_error_message(self, value):
        print('value is', value)
        if value != '410':
            self.player.numb_errors = 1
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей ' \
                   'попытки ввода неверного значения'

    def task_6_error_message(self, value):
        print('value is', value)
        if value != 4:
            self.player.numb_errors = 1
            return 'пожалуйста проверьте правильность введнного ответа, поднимите руку после третьей ' \
                   'попытки ввода неверного значения'

    def before_next_page(self):
        agent = self.group.get_player_by_role('agent')
        principal = self.group.get_player_by_role('principal')
        agent.participant.vars['info_for_principal_agent_q1'] = agent.social_media_time_spend
        agent.participant.vars['info_for_principal_agent_q2'] = agent.numb_of_last_books
        principal.participant.vars['info_for_principal_agent_risk_among_oth'] = agent.average_plrs_risk

class IntroductionWaitPage2(WaitPage):

    def after_all_players_arrive(self):
        self.group.show_prefference_to_principal()

class Offer(Page):
    timeout_seconds = 180

    def vars_for_template(self):
         r_am_oth = self.participant.vars['info_for_principal_agent_risk_among_oth']
         return dict( r_am_oth = r_am_oth)

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
            body_text = "Ваша роль Исполнитель, ожидайте пока Заказчик составит для Вас условия контракта."
        else:
            body_text = "Ожидайте Участника в роли Исполнителя."
        return {'body_text': body_text}


    def after_all_players_arrive(self):
        self.group.randome_move_solver()
        if Constants.session_swicher != 1:
            self.group.robot_moves_principal()


class Accept(Page):
    timeout_seconds = 180
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

    form_model = 'player'

    def vars_for_template(self):
        if self.round_number == Constants.num_rounds:
             a = []
             b = []
             for i in range(1, Constants.num_rounds+1):
                 a.append(i)
                 b.append(self.player.in_round(i).payoff)
             lottery = self.player.participant.vars['pl_mpl_payoff']
             return dict(lottery = lottery, payset = zip(a, b,) )


    pass




page_sequence = [PreWaitPage,
                 IntroductionWaitPage,
                 question,
                 Introduction,
                 quiz,
                 IntroductionWaitPage2,
                 Offer,
                 OfferWaitPage,
                 Accept,
                 ResultsWaitPage,
                 Results]

