from abc import ABCMeta , abstractmethod
class Figure (metaclass=ABCMeta):
    """Абстрактный класс фигура"""
    FIGURE_TYPE = ""

    def __init__(self):
        pass
    """функция для вычисления площади фигуры"""
    @abstractmethod
    def square_fig(self):
        pass
    def get_figure_type(self):
        return self.FIGURE_TYPE

