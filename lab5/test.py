# test_field.py
import unittest
from lab4 import field

class TestFieldFunction(unittest.TestCase):
    def setUp(self):
        self.goods = [
            {'title': 'Ковер', 'price': 2000, 'color': 'green'},
            {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
        ]

    def test_extract_single_field(self):
        titles = list(field(self.goods, 'title'))
        self.assertEqual(titles, ['Ковер', 'Диван для отдыха'])

    def test_extract_multiple_fields(self):
        prices = list(field(self.goods, 'title', 'price'))
        expected = [
            {'title': 'Ковер', 'price': 2000},
            {'title': 'Диван для отдыха', 'price': 5300}
        ]
        self.assertEqual(prices, expected)

    def test_extract_non_existent_field(self):
        result = list(field(self.goods, 'non_existent_field'))
        self.assertEqual(result, [])

    def test_get_all_list(self):
        result = list(field(self.goods, 'title', 'price','color'))
        expected = [
            {'title': 'Ковер', 'price': 2000, 'color': 'green'},
            {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()