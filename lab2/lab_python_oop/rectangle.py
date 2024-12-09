from lab_python_oop.figure import Figure
from lab_python_oop.color import Color


class Rectangle(Figure):

    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, color, w, h):

        self.width = w
        self.height = h
        self.rect_col = Color()
        self.rect_col.col = color
    def square_fig(self):
        return self.width*self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            self.get_figure_type(),
            self.rect_col.col,
            self.width,
            self.height,
            self.square_fig()
        )