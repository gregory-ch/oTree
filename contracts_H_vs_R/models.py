from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools
author = 'BeLab HSE'

doc = """
Your app description
"""

# заменяю все  cons.r  на self.participant.vars['r_coef']

class Constants(BaseConstants):
    name_in_url = 'contracts_H_vs_R'
    players_per_group = 2
    num_rounds = 20
    instructions_template = 'contracts_H_vs_R/instructions.html'

    min_efforts = 0
    max_efforts = 10
    reject_principal_pay = c(0)
    reject_agent_pay = c(0)

    min_fixed_payment = c(0)
    max_fixed_payment = c(100)

    min_piece_payment = c(0)
    max_piece_payment = c(10)
    mu = 0
    sigma = 4/3
    s = 10 # coeff of production function
    # r = 1 # risk aversion coefficient of all agents (later will be changed to individual)

    risk_avers_for_exp_shape = {
        1: 0.5625,
        2: 0.5625,
        3: 0.5625,
        4: 0.5625,
        5: 0.5625,
        6: 0.57364266,
        7: 0.84197484,
        8: 1.25999558,
        9: 20.30937094,
        10: 377,
        11: 377
    }



class Subsession(BaseSubsession):

    # separation population on Hum vs Hum and Hum vs Robot

    def creating_session(self):
        gtypes = itertools.cycle(['HH', 'HR'])

        for g in self.get_groups():
            if self.round_number == 1:
                gtype = next(gtypes)
                g.gtype = gtype
            else:
                g.gtype = g.in_round(1).gtype


class Group(BaseGroup):
    gtype = models.StringField()
    # General and Hum vs Hum variables

    def return_from_effort(self, effort):
        return (effort + self.epsilon) * Constants.s

    total_return = models.CurrencyField(
        doc="""Общая выручка = [коэфицициент производства (s)] * [Усилия Агента + epsilon]"""
    )

    agent_last_risk_choice = models.FloatField(
        doc="""отношение к риску вашего оппонента"""
    )

    agent_average_risk_choice =  models.FloatField(
        doc="""среднее отношение к риску вашего оппонента по трем раундам"""
    )
    agent_fixed_pay = models.CurrencyField(
        doc="""фиксированная оплата, котороую вы хотите предложить агенту""",
        min=Constants.min_fixed_payment, max=Constants.max_fixed_payment,
    )

    agent_piece_rate = models.FloatField(
        doc="""Cдельная оплата за результат, котороую вы хотите предложить агенту""",
        min=Constants.min_piece_payment, max=Constants.max_piece_payment,
    )

    Hum_effort = models.FloatField(
        doc="""Количество усилий которые вы хотите затратить""",
        min=Constants.min_efforts , max=Constants.max_efforts ,
    )


    # Hum vs Robot variables

    total_return_Hum_A_vs_robot = models.CurrencyField()
    total_return_Hum_P_vs_robot = models.CurrencyField()
    robot_agent_offer_fixed_pay = models.CurrencyField()
    robot_agent_offer_piece_rate = models.FloatField()
    robot_effort = models.FloatField()
    eff_plus_eps = models.FloatField()
    eff_plus_eps_r = models.FloatField()
    swicher = models.StringField()

    # functions start

    epsilon = models.FloatField()  # - random variable computation, нужно не забыть ограничить
    def randome_move_solver(self):
        self.epsilon = round( random.normalvariate(Constants.mu, Constants.sigma),2)

    # starts payoff calculation

    def robot_moves_principal(self):
        agent = self.get_player_by_role('agent')
        if self.round_number == 1:
            self.swicher = 'HR'
        else:
            self.swicher = 'HH'
        if self.gtype != self.swicher:
            if agent.risk_coeff > 0.521:
                self.robot_agent_offer_piece_rate = round( Constants.s/(1+agent.risk_coeff *(Constants.sigma**2)),2)
                self.robot_agent_offer_fixed_pay = round( 1 - (self.robot_agent_offer_piece_rate**2)/2 + agent.risk_coeff*(self.robot_agent_offer_piece_rate**2)*(Constants.sigma**2)/2, 2)
            else:
                self.robot_agent_offer_piece_rate = 5
                self.robot_agent_offer_fixed_pay = 0


    def x_counter_H (self):
         self.eff_plus_eps = self.Hum_effort + self.epsilon

    def x_counter_R (self):
        if self.gtype != self.swicher:
            self.eff_plus_eps_r = self.robot_effort + self.epsilon

    def risk_counter(self):
        agent = self.get_player_by_role('agent')
        self.agent_last_risk_choice = sum(agent.participant.vars['mpl_choices_made']) + 1
        self.agent_average_risk_choice = round(agent.participant.vars['av_switching_row_for_rounds'])
        for p in self.get_players():
            p.risk_choice = sum(p.participant.vars['mpl_choices_made']) + 1
            p.risk_coeff = Constants.risk_avers_for_exp_shape[round(p.participant.vars['av_switching_row_for_rounds'])]






    def set_payoffs(self):
        principal = self.get_player_by_role('principal')
        agent = self.get_player_by_role('agent')
        if self.gtype == self.swicher:
            self.total_return = self.return_from_effort(self.Hum_effort)
            money_to_agent = self.agent_piece_rate*(self.Hum_effort+self.epsilon)+ self.agent_fixed_pay
            agent.payoff = money_to_agent - 0.5 * (self.Hum_effort**(2))
            random_seed = random.random()
            principal_prob = (self.total_return - money_to_agent)/ 25
            if principal_prob >= random_seed:
                principal.payoff = 20
            else:
                principal.payoff = 0

        else:
            self.total_return_Hum_A_vs_robot = self.return_from_effort(self.Hum_effort)
            money_to_agent = self.robot_agent_offer_piece_rate*(self.Hum_effort+self.epsilon)+self.robot_agent_offer_fixed_pay
            agent.payoff = money_to_agent - 0.5 * (self.Hum_effort ** (2))
            random_seed = random.random()
            etalon_beta= 1-0.5*self.agent_piece_rate**2+0.5*agent.risk_coeff*(Constants.sigma**2)*self.agent_piece_rate**2
            if self.agent_fixed_pay >= etalon_beta:
                self.robot_effort = self.agent_piece_rate
                self.total_return_Hum_P_vs_robot = self.return_from_effort(self.robot_effort)
                money_to_robot_agent = self.agent_piece_rate*(self.robot_effort+self.epsilon)+ self.agent_fixed_pay
                principal_prob= (self.total_return_Hum_P_vs_robot - money_to_robot_agent)/25
                if principal_prob >= random_seed:
                    principal.payoff = 20
                else:
                    principal.payoff = 0
            else:
                self.total_return_Hum_P_vs_robot = 0
                self.robot_effort = 0
                principal.payoff = 0





class Player(BasePlayer):

    risk_coeff = models.FloatField()
    risk_choice = models.FloatField()
    numb_errors = models.FloatField()
    def role(self):
        if self.id_in_group == 1:
            return 'principal'
        else:
            return 'agent'

    task_1 = models.StringField(
        label='Задание 1. Во втором этапе Участник 2 выбрал уровень усилий 2,5  на шаге 2. '
              'На шаге 3 компьютер посчитал значение Случайного фактора, оно составило  1,5. '
              'Каков будет общий заработок обоих участников?')
    task_2 = models.StringField(
        label='Задание 2. Во втором этапе  Участник 1 на шаге 1 в первом раунде предложил фиксированную часть вознаграждения'
              ' в размере 9, и переменную часть в размере 2.  Участник 2 предпринял усилия 4и '
              'компьютер на шаге 3 считал значение удачи, оно составло - 1. Какова вероятность того, что участник 1 получит 20 токенов за раунд?')

    task_3 = models.StringField(
        label='Какова вероятность того, что участник 1 получит 0 токенов за раунд?')

    task_4 = models.StringField(
        label='Сколько получит участник 2? ')

    task_5 = models.StringField(
        label='Задание 3. Участник 2  на втором этапе в течение 20 раундов выигрывал в каждом раунде по 12 токенов, на первом этапе'
              ' 1, токена без учета поправочного коэфициента. Сколько рублей в конце эксеримента получит участник? '
              '(для использования 10-й записи используйте точку как разделитель)')

    task_6 = models.IntegerField(
        label=' Задание 4. Выберите правильный ответ на вопрос:  Участник 2 в одном из раундов второго этапа, выбрал уровень усилий'
              ' в размере 6. Какова вероятность что результат усилий с учетом удачи выйдет из интервала от 3 '
              'до 9 ?',
        choices=[   [1 , '50%'],
                    [2 , 'Приближается к 100%'],
                    [3 , '95%'],
                    [4 , 'Приближается к 1%'],
                    [5 , '5%'],
                    ]
        )
