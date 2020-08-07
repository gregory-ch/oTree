from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey_rps'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

        # def set_payoff(self):
        #     """Calculate payoff, which is zero for the survey"""
        #         self.payoff = 0

    age = models.PositiveIntegerField(verbose_name='Ваш возраст (полных лет)',
                                      min=13, max=95,
                                      initial=None)

    gender = models.BooleanField(initial=None,
                                 choices=[[0, 'Мужской'], [1, 'Женский']],
                                 verbose_name='Ваш пол',
                                 widget=widgets.RadioSelect())

    height = models.PositiveIntegerField(verbose_name='Ваш рост (в сантиметрах)',
                                         min=100, max=240,
                                         initial=None)

    guess = models.PositiveIntegerField(verbose_name='загатайте целое число от 1 до 10',
                                      min=0, max=10,
                                      initial=None)

    city = models.PositiveIntegerField(
        verbose_name='''
    Сколько человек (приблизительно) проживало в том населенном пункте, где Вы жили в возрасте 16 лет.''',
        min=1, max=30000000,
        initial=None)

    math = models.PositiveIntegerField(
        verbose_name='''как вы оцениваете свои знания в математике»)''',
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal()
    )

    tigr = models.BooleanField(initial=None,
                                 choices=[[0, 'нет'], [1, 'да']],
                                 verbose_name='Проходили ли вы курс по теории игр',
                                 widget=widgets.RadioSelect())

    equi = models.StringField(
        verbose_name='''Какие равновесия есть в игре "Камень-Ножницы-Бумага"? (впишите "не знаю" если не знаете как ответить на этот вопрос)'''
    )

    trend0 = models.BooleanField(initial=None,
                                 choices=[[0, 'нет'], [1, 'да']],
                                 verbose_name='как вам кажется подчинялся ли алгоритм оппонента конкретным правилам?',
                                 widget=widgets.RadioSelect())


    trend2 = models.StringField(
        verbose_name='''Пожалуйста ответьте максимально подробно! Если вы заметили какую-либо закономерность в работе программы, пожалуйста опишите её, а так же приблизительный номер раунда в котором вы её заметили.'''
    )

    univ = models.StringField(
        verbose_name='''Укажите вуз, в котором Вы получили последнюю ступень вашего высшего образования.'''
    )



    satis = models.PositiveIntegerField(
        verbose_name='''Учитывая все обстоятельства, насколько Вы удовлетворены вашей жизнью в целом в эти дни? (от 1 «полностью не удовлетворен» до 10 «полностью удовлетворен»)''',
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal()
    )

    trust = models.PositiveIntegerField(
        verbose_name='''Как Вы считаете, в целом большинству людей можно доверять, или же при общении с другими людьми 
        осторожность никогда не повредит? Пожалуйста, отметьте позицию на шкале, где 1 означает "Нужно быть очень осторожным с другими людьми" и 10
        означает "Большинству людей можно вполне доверять" ''',
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal()
    )

