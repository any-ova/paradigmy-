import math
import unittest
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

class Test_Rect(unittest.TestCase):
    '''тесты для класса прямоугольник'''
    def test_rec(self):
        R1=Rectangle("красный",1,2)
        self.assertEqual(R1.square_fig(),2)
        self.assertEqual(R1.rect_col.col, "красный")
        self.assertEqual(R1.width, 1)
        self.assertEqual(R1.height, 2)
class Test_Square(unittest.TestCase):
    def test_sqr(self):
        S1 = Square("синий", 5)
        self.assertEqual(S1.square_fig(), 25)
        self.assertEqual(S1.rect_col.col, "синий")
        self.assertEqual(S1.side, 5)

class Test_Circle(unittest.TestCase):
    def test_cir(self):
        S1 = Circle("зелёный", 25)
        self.assertEqual(S1.square_fig(), 625*math.pi)
        self.assertEqual(S1.circ_col.col, "зелёный")
        self.assertEqual(S1.radius, 25)




if __name__ == '__main__':
    unittest.main()