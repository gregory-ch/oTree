from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'c_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(
        label='Ваш возраст',
        min=15, max=65
    )


    height = models.IntegerField(
        label='Ваш рост в см',
        min=50, max=210)

    gender = models.StringField(
        choices=['Мужской', 'Женский'],
        label='Ваш пол',
        widget=widgets.RadioSelect)

    state = models.StringField(
        label='Ваш факультет, 0 если неприменимо')

    education = models.StringField(
        choices=['Начальное или неполное среднее', 'Среднее (закончили школу)',
                 'Среднее профессиональное (техникум, училище)', 'Диплом бакалавра', 'Диплом специалиста',
                 'Диплом магистра', 'Аспирантура без получения учёной степени', 'Кандидат наук', 'Доктор наук'],
        label='Ваш самый высокий уровень образования',
        widget=widgets.RadioSelect)

    wage = models.IntegerField(
        label='Ваш средний месячный доход, 0 если неприменимо',
        min=0, max=150000)

    experience = models.StringField(
        choices=['Да', 'Нет'],
        label='Принимали ли вы участие в экспериментах раньше?',
        widget=widgets.RadioSelect)

    mark = models.IntegerField(
        label='Балл за ЕГЭ по математике (укажите 0, если не помните)',
        min=0, max=100)

    loneliness = models.StringField(
        choices=['Почти всегда', 'Часто', 'Редко', 'Почти никогда'],
        label='Вы испытываете чувство одиночества?',
        widget=widgets.RadioSelect)

    trust = models.StringField(
        choices=['Большинству людей можно доверять', 'С людьми всегда надо быть осторожным',
                 'И то, и другое в зависимости от человека, условий'],
        label='Считаете ли вы, что большинству людей можно доверять или что в отношениях с людьми всегда надо быть'
              ' осторожным?',
        widget=widgets.RadioSelect)

    max_satisf_min_1 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' Вне зависимости от того, насколько я доволен своей работой, мне кажется правильным искать лучшие возможности ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_2 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' Вне зависимости от того, что я делаю, я предъявляю к себе самые высокие требования ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_3 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' Я никогда не довольствуюсь чем-то второсортным ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_4 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' Когда я выбираю из альтернатив, я останавливаюсь на первом варианте, который мне подходит ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_5 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' На работе или в учебе я всегда ставлю самые высокие цели ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_6 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' На работе или в учебе я склонен выбирать решения, которые гарантируют удовлетворяющие меня результаты ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_7 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' На работе или в учебе я ставлю цели, для достижения которых требуется минимальное усилие ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_8 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' Всякий раз, когда я делаю выбор, я пытаюсь представить все альтернативы, даже те, которые отсутствуют в данный момент ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_9 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' На работе или в учебе я согласен с любым выбором, который приносит минимальный результат ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_10 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' В любой области я пытаюсь достичь удовлетворяющих меня результатов ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_11 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' На работе или в учебе даже минимальный результат может меня устроить ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_12 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' На работе или в учебе я трачу время на то, чтобы выбрать решение, которое меня устраивает ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_13 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' Я всегда ставлю цели, для достижения которых требуется минимальное усилие ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_14 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' Когда я принимаю решения, я трачу время на то, чтобы выбрать приемлемую для себя альтернативу ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_15 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' Когда я должен принять решение, я выбираю вариант "по - минимуму" ',
    widget = widgets.RadioSelectHorizontal
    )
    max_satisf_min_16 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' Когда передо мной встает новая задача, я трачу много времени на сбор информации о возможных путях ее решения ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_17 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' Когда на работе мне дают новое задание, я прилагаю не больше усилий, чем требуется ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_18 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' При выполнении рабочего задания я стремлюсь к максимальному результату, не считая потраченные силы и время ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_19 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' При выполнении любого задания я удовлетворяюсь результатом, который считаю достаточным на данный момент ',
        widget=widgets.RadioSelectHorizontal
    )
    max_satisf_min_20 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=' При выполнения рабочего задания меня устроит результат, для достижения которого требуется минимум усилий ',
        widget=widgets.RadioSelectHorizontal
    )


