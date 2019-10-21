from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from numpy import random as rdm
import itertools
author = 'BeLab HSE'

doc = """
Your app description
"""

# заменяю все  cons.r  на self.participant.vars['r_coef']

class Constants(BaseConstants):
    name_in_url = 'contracts_H_vs_R'
    players_per_group = 2
    num_rounds = 2
    instructions_template = 'contracts_H_vs_R/instructions.html'


    session_swicher  =  1
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
    high_payoff = c(40)
    low_payoff = c(10)
    s = 10 # coeff of production function


    risk_avers_for_exp_shape = {
        1: 0.5625,
        2: 0.5625,
        3: 0.5625,
        4: 0.582,
        5: 0.680,
        6: 0.797,
        7: 0.944,
        8: 1.149,
        9: 11.83,
        10: 255,
        11: 255
    }



class Subsession(BaseSubsession):

    # separation population on Hum vs Hum and Hum vs Robot

    def creating_session(self):

        if Constants.session_swicher == 1 :
            gtypes = itertools.cycle(['HH'])
        else:
            gtypes = itertools.cycle(['HH', 'HR'])

        for g in self.get_groups():
            if self.round_number == 1:
                gtype = next(gtypes)
                g.gtype = gtype
            else:
                g.gtype = g.in_round(1).gtype

    def avarege_risk_counter(self):
        choices=[]
        for pl in self.get_players():
            choices.append(pl.participant.vars['av_switching_row_for_rounds'] )

        for pl in self.get_players():
            pl.avarege_plrs_risk = sum(choices)/len(choices)



class Group(BaseGroup):
    gtype = models.StringField()
    # General and Hum vs Hum variables
    realized_rounds_1 = models.FloatField()
    realized_rounds_2 = models.FloatField()


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

    agent_q_1 = models.IntegerField(
            )
    agent_q_2  = models.IntegerField(
    )


    agent_piece_rate = models.FloatField(
        doc="""Cдельная оплата за результат, котороую вы хотите предложить агенту""",
        min=Constants.min_piece_payment, max=Constants.max_piece_payment,
    )

    expected_efforts = models.FloatField(
        doc="""какое количество усилий, как вам кажется, предложит агент """,
        min=Constants.min_piece_payment, max=Constants.max_piece_payment,
    )

    Hum_effort = models.FloatField(
        doc="""Количество усилий которые вы хотите затратить""",
        min=Constants.min_efforts , max=Constants.max_efforts ,
    )
    viewed_risk_preff  = models.IntegerField(
        doc="""просмотр предпочтений оппонента""",
    )
    viewed_social_media_time_spend  = models.IntegerField(
        doc="""просмотр времени потраченного на соцсети""",
    )

    viewed_numb_of_last_books  = models.IntegerField(
        doc="""просмотр приблизительного колличества прочитанных книг""",
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
            if agent.risk_coeff > 0.5625:
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
        self.agent_q_1 = agent.social_media_time_spend
        self.agent_q_2 = agent.numb_of_last_books
        for p in self.get_players():
            p.risk_choice = sum(p.participant.vars['mpl_choices_made']) + 1
            p.risk_coeff = Constants.risk_avers_for_exp_shape[round(p.participant.vars['av_switching_row_for_rounds'])]
            if self.round_number > 1:
                p.social_media_time_spend = p.in_round(self.round_number - 1).social_media_time_spend
                p.numb_of_last_books = p.in_round(self.round_number - 1).numb_of_last_books


    def set_swicher(self):
        if Constants.session_swicher == 1:
            self.swicher = 'HH'


    def set_payoffs(self):
        principal = self.get_player_by_role('principal')
        agent = self.get_player_by_role('agent')
        if self.gtype == self.swicher:
            self.total_return = self.return_from_effort(self.Hum_effort)
            money_to_agent = self.agent_piece_rate*(self.Hum_effort+self.epsilon)+ self.agent_fixed_pay
            agent.payoff = money_to_agent - 0.5 * (self.Hum_effort**(2))
            random_seed = random.random()
            principal.payoff = (self.total_return - money_to_agent)


        else:
            self.total_return_Hum_A_vs_robot = self.return_from_effort(self.Hum_effort)
            money_to_agent = self.robot_agent_offer_piece_rate*(self.Hum_effort+self.epsilon)+self.robot_agent_offer_fixed_pay
            agent.payoff = money_to_agent - 0.5 * (self.Hum_effort ** (2))
            random_seed = random.random()
            etalon_beta= -0.5*self.agent_piece_rate**2+0.5*agent.risk_coeff*(Constants.sigma**2)*self.agent_piece_rate**2
            if self.agent_fixed_pay >= etalon_beta:
                self.robot_effort = self.agent_piece_rate
                self.total_return_Hum_P_vs_robot = self.return_from_effort(self.robot_effort)
                money_to_robot_agent = self.agent_piece_rate*(self.robot_effort+self.epsilon)+ self.agent_fixed_pay
                principal.payoff= (self.total_return_Hum_P_vs_robot - money_to_robot_agent)

            else:
                self.total_return_Hum_P_vs_robot = 0
                self.robot_effort = 0
                principal.payoff = 0

    def final_payoff (self):
        if self.round_number  == Constants.num_rounds:
            self.realized_rounds_1 = random.randint(1, Constants.num_rounds)
            self.realized_rounds_2 = random.randint(1, Constants.num_rounds)
            while self.realized_rounds_1 == self.realized_rounds_2:
                self.realized_rounds_2 = random.randint(1, Constants.num_rounds)
            for p in self.get_players():
                p.participant.payoff = p.in_round(self.realized_rounds_1
                ).payoff + p.in_round(self.realized_rounds_2).payoff + p.participant.vars['pl_mpl_payoff']
                if p.participant.payoff < 0 :
                    p.participant.payoff = 0
            principal = self.get_player_by_role('principal')
            if principal.participant.payoff <= 50:
                if principal.participant.payoff <= 0:
                    principal.participant.payoff = Constants.low_payoff
                else: 
                    principal.participant.payoff = rdm.choice([Constants.high_payoff, Constants.low_payoff],  p=[float(principal.payoff) / 50, 1 - float(principal.payoff) / 50])
            else:
                principal.participant.payoff = Constants.high_payoff






class Player(BasePlayer):

    risk_coeff = models.FloatField()
    risk_choice = models.FloatField()
    numb_errors = models.FloatField()
    avarege_plrs_risk = models.FloatField()





    def role(self):
        if self.id_in_group == 1:
            return 'principal'
        else:
            return 'agent'

    task_1 = models.StringField(
        label='Задание 1. Во втором этапе Участник 2 выбрал уровень усилий 2,5  на шаге 2. '
              'На шаге 3 компьютер посчитал значение Случайного фактора, оно составило  1,5. '
              'Какова будет Выручка Участника 1?')
    task_2 = models.StringField(
        label='Задание 2. Во втором этапе  Участник 1 на шаге 1 в первом раунде предложил фиксированную часть вознаграждения '
              ' в размере 9, и переменную часть в размере 2.  Участник 2 предпринял усилия 4 и '
              'компьютер на шаге 3 выбрал значение случайного фактора, оно составло - 1. Сколько токентов получит Участник 1 за раунд?')

    task_3 = models.StringField(
        label='Предположим что результат повторился и компьютр выбрал оба результата в качестве выплат за этап 2. '
              'Какова вероятность того, что участник 1 получит 10 токенов за этап 2 ?')

    task_4 = models.StringField(
        label='Сколько получит Участник 2? ')

    task_5 = models.StringField(
        label='Задание 3. Участник 2  на втором этапе в течение 20 раундов выигрывал в каждом раунде по 12 токенов, на первом этапе '
              '23 токена. Сколько рублей в конце эксеримента получит участник? '
              '(для использования 10-й записи используйте точку как разделитель)')

    task_6 = models.IntegerField(
        label=' Задание 4. Выберите правильный ответ на вопрос:  Участник 2 в одном из раундов второго этапа, выбрал уровень усилий '
              ' в размере 6. Какова вероятность что результат усилий с учетом случайного фактора выйдет из интервала от 3 '
              'до 9 ?',
        choices=[   [1 , '50%'],
                    [2 , 'Приближается к 100%'],
                    [3 , '95%'],
                    [4 , 'Приближается к 1%'],
                    [5 , '5%'],
                    ]
        )


    social_media_time_spend = models.IntegerField(
        label= 'Дополнительно происим ответить на 2 следующих вопроса (информация о ваших ответах, только на эти два '
              'вопроса будет доступна другим участникам). '
              'Укажите приблизительное колличество стран, которое вы посетили?', min = 0, max = 100)

    numb_of_last_books = models.IntegerField(
        label='укажите приблизительное колличество книг, прочитанных вами за последние три месяца', min = 0, max = 20)