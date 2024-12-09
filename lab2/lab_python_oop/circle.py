from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
import math

class Circle(Figure):
    FIGURE_TYPE = "Круг"

    def __init__(self, color, rad):
        self.radius = rad
        self.circ_col = Color()
        self.circ_col._color = color
    def square_fig(self):
        return math.pi*(self.radius**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {:.4f}.'.format(
            self.get_figure_type(),
            self.circ_col.col,
            self.radius,
            self.square_fig()
        )