from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class MyPage(Page):
    form_model = 'player'

    form_fields = ['y']

    def before_next_page(self):
        self.player.random_item()
        self.player.count_num_square()



class Results(Page):
    form_model = 'player'
    def vars_for_template(self):
        # dict_ = {}
        # for i in range(16):
        #     key = 'z_'+ str(i)
        #     dict_[key] = [random.randrange(-1, 2, 2)*5+self.player.x]
        # # return {'z': [random.randrange(-1, 2, 2)*5+self.player.x for i in range(16)]}
        z = []
        w = []
        return {'z': [round(random.choice([-2,-1,1,2]) * 6
                            * (self.player.y**0.5)) + self.player.x for i in range(16)],'w' : z.insert(random.randrange(0, 15), 0)}

        # dict_with_endowments_and_unit_values = {}
        # for i in range(12):
        #     key = 'endowment_iter_' + str(i + 1)
        #     dict_with_endowments_and_unit_values[key] = models.Constants.endowments_list[i]
        #     key = 'unit_values_for_S_iter_' + str(i + 1)
        #     dict_with_endowments_and_unit_values[key] = models.Constants.unit_values_for_S_list[i]
        #     key = 'unit_values_for_R_iter_' + str(i + 1)
        #     dict_with_endowments_and_unit_values[key] = models.Constants.unit_values_for_R_list[i]

        # return {'y': [k * 5 for k in z]}
        # return {'w': self.y.insert(random.randrange(0, 15), 0)}


        # return {'q': [i + player.x for i in w]}

     # def vars_for_template(self):
     #    return {'z': [random.randrange(-1, 2, 2) for i in range(16)], 'y': [k * 5 for k in z], 'w': y.insert(random.randrange(0, 15), 0),
     #        'q': [i + x for i in y]}

page_sequence = [
    MyPage,
    Results
]
