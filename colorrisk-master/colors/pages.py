from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from colormath.color_objects import LabColor, HSLColor
from colormath.color_conversions import convert_color
import numpy




class Choice(Page):
    form_model = 'player'
    form_fields = ['step']

    def vars_for_template(self) -> dict:
        def get_numpy_array(self):
            values = []
            for val in self.VALUES:
                values.append(getattr(self, val, 0.0))
            color_array = numpy.array(values)
            return color_array
        lab_colors = [LabColor(Constants.hue, i, Constants.saturation) for i in
                  self.player.get_max_colors()]
        example = [get_numpy_array(convert_color(lab_colors[i], HSLColor)) for i in
                  range(len(lab_colors))]

        colors = [{'hue': 100*example[i][0], 'saturation': 100*example[i][1], 'lightness': 100*example[i][2]} for i in
                  range(len(lab_colors))]
        payoffs = Constants.payoffs
        choices = self.get_form()["step"]

        return {'colorset': zip(colors, payoffs, choices)}

    def before_next_page(self):
        self.player.generate_colors()


class Task(Page):
    form_model = 'player'
    form_fields = ['answer']

    def vars_for_template(self) -> dict:
        step = 1
        return {'colors': [step * i for i in range(1, 17)]}

    def before_next_page(self):
        self.player.set_answered_color()
        self.player.set_payoff()


class Results(Page):
    pass


page_sequence = [
    Choice,
    Task,
    Results
]
