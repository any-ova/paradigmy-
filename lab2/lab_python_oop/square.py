from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, col, a):
        self.side = a
        super().__init__(col, self.side, self.side)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            self.get_figure_type(),
            self.rect_col.col,
            self.side,
            self.square_fig()
        )