from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 10.00,
    'participation_fee': 0.00,
    'doc': "",

}

SESSION_CONFIGS = [
    {
        'name': 'public_goods',
        'display_name': "Public Goods",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods', 'payment_info', 'my_survey'],
    },
    {
        'name': 'guess_two_thirds',
        'display_name': "Guess 2/3 of the Average",
        'num_demo_participants': 3,
        'app_sequence': ['guess_two_thirds', 'payment_info'],
    },
    # {
    #     'name': 'survey',
    #     'num_demo_participants': 1,
    #     'app_sequence': ['survey', 'payment_info'],
    # },
    # {
    #     'name': 'quiz',
    #     'num_demo_participants': 1,
    #     'app_sequence': ['quiz'],
    # },

    # {
    # 'name': 'principal_agent',
    # 'display_name': "Principal Agent",
    # 'num_demo_participants': 2,
    # 'app_sequence': ['principal_agent', 'payment_info'],
    # },



    {
        'name': 'trains',
        'display_name': "trains",
        'num_demo_participants': 10,
        'app_sequence': ['trains']
    },

    # {
    #     'name': 'color_table',
    #     'display_name': "color_table",
    #     'num_demo_participants': 10,
    #     'app_sequence': ['color_table']
    # },
    {
        'name': 'Contracts_H_VS_R',
        'display_name': "Contracts_H_VS_R",
        'num_demo_participants': 2,
        'app_sequence': ['mpl', 'contracts_H_vs_R', 'my_survey'],
        # 'app_sequence': ['mpl'],
        'use_browser_bots': False
    },
    #
    # {
    #     'name': 'bret',
    #     'display_name': "bret",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['bret'],
    #     },
{
        'name': 'roshambo',
        'display_name': "roshambo",
        'num_demo_participants': 1,
        'app_sequence': ['roshambo'],
        },

    #
]
# see the end of this file for the inactive session configs


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ru'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'RUR'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'токен'

ROOMS = [

    {'name': 'HSE',
     'display_name': 'Lsh_workshop'},
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
]

OTREE_PRODUCTION = True
ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = ')3hndu0o6bq_o&27$q*)$7f(l-w+gje2nitakiv+hxj(#g2lcv'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# inactive session configs
### {
###     'name': 'trust',
###     'display_name': "Trust Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust', 'payment_info'],
### },
### {
###     'name': 'prisoner',
###     'display_name': "Prisoner's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['prisoner', 'payment_info'],
### },
### {
###     'name': 'ultimatum',
###     'display_name': "Ultimatum (randomized: strategy vs. direct response)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
### },
### {
###     'name': 'ultimatum_strategy',
###     'display_name': "Ultimatum (strategy method treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': True,
### },
### {
###     'name': 'ultimatum_non_strategy',
###     'display_name': "Ultimatum (direct response treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': False,
### },
# {
#     'name': 'vickrey_auction',
#     'display_name': "Vickrey Auction",
#     'num_demo_participants': 3,
#     'app_sequence': ['vickrey_auction', 'payment_info'],
# },
### {
###     'name': 'volunteer_dilemma',
###     'display_name': "Volunteer's Dilemma",
###     'num_demo_participants': 3,
###     'app_sequence': ['volunteer_dilemma', 'payment_info'],
### },
# {
#     'name': 'cournot',
#     'display_name': "Cournot Competition",
#     'num_demo_participants': 2,
#     'app_sequence': [
#         'cournot', 'payment_info'
#     ],
# },
###
### {
###     'name': 'dictator',
###     'display_name': "Dictator Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['dictator', 'payment_info'],
### },
### {
###     'name': 'matching_pennies',
###     'display_name': "Matching Pennies",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'matching_pennies',
###     ],
### },
# {
#     'name': 'traveler_dilemma',
#     'display_name': "Traveler's Dilemma",
#     'num_demo_participants': 2,
#     'app_sequence': ['traveler_dilemma', 'payment_info'],
# },
# {
#     'name': 'bargaining',
#     'display_name': "Bargaining Game",
#     'num_demo_participants': 2,
#     'app_sequence': ['bargaining', 'payment_info'],
# },
# {
#     'name': 'common_value_auction',
#     'display_name': "Common Value Auction",
#     'num_demo_participants': 3,
#     'app_sequence': ['common_value_auction', 'payment_info'],
# },
# {
#     'name': 'bertrand',
#     'display_name': "Bertrand Competition",
#     'num_demo_participants': 2,
#     'app_sequence': [
#         'bertrand', 'payment_info'
#     ],
# },
### {
###     'name': 'real_effort',
###     'display_name': "Real-effort transcription task",
###     'num_demo_participants': 1,
###     'app_sequence': [
###         'real_effort',
###     ],
### },
# {
#     'name': 'lemon_market',
#     'display_name': "Lemon Market Game",
#     'num_demo_participants': 3,
#     'app_sequence': [
#         'lemon_market', 'payment_info'
#     ],
# },
### {
###     'name': 'public_goods_simple',
###     'display_name': "Public Goods (simple version from tutorial)",
###     'num_demo_participants': 3,
###     'app_sequence': ['public_goods_simple', 'payment_info'],
### },
### {
###     'name': 'trust_simple',
###     'display_name': "Trust Game (simple version from tutorial)",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust_simple'],
### },