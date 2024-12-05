import unittest
from music import MusicalPiece, Orchestra, MusicOrch, get_one_to_many, get_many_to_many, task_a1, task_a2, task_a3


class TestMusic(unittest.TestCase):
    def setUp(self):
        """Инициализация данных для тестов"""
        self.orch = [
            Orchestra(1, 'Оркестр имени Чайковского'),
            Orchestra(2, 'Народный Оркестр'),
            Orchestra(3, 'Камерный оркестр Карелии'),
        ]

        self.mus = [
            MusicalPiece(1, 'Симфония №1', 120, 1),
            MusicalPiece(2, 'Симфония №3', 40, 2),
            MusicalPiece(3, 'Увертюра', 15, 3),
        ]

        self.music_orch = [
            MusicOrch(1, 1),
            MusicOrch(2, 2),
            MusicOrch(3, 3),
        ]

    def test_task_a1(self):
        one_to_many = get_one_to_many(self.orch, self.mus)
        result = task_a1(one_to_many)
        expected = sorted([
            ('Симфония №1', 120, 'Оркестр имени Чайковского'),
            ('Симфония №3', 40, 'Народный Оркестр'),
            ('Увертюра', 15, 'Камерный оркестр Карелии'),
        ], key=lambda x: x[2])  # Ожидаемый результат отсортирован по названию оркестра
        self.assertEqual(result, expected)

    def test_task_a2(self):
        one_to_many = get_one_to_many(self.orch, self.mus)
        result = task_a2(one_to_many, self.orch)
        expected = sorted([
            ('Оркестр имени Чайковского', 120),
            ('Народный Оркестр', 40),
            ('Камерный оркестр Карелии', 15),
        ], key=lambda x: x[1], reverse=True)  # Сортировка по длительности произведений
        self.assertEqual(result, expected)

    def test_task_a3(self):
        many_to_many = get_many_to_many(self.orch, self.mus, self.music_orch)
        result = task_a3(many_to_many, self.orch)
        expected = {
            'Оркестр имени Чайковского': ['Симфония №1'],
            'Народный Оркестр': ['Симфония №3'],
        }  # Учитываются только оркестры, содержащие "Оркестр" в названии
        self.assertDictEqual(result, expected)


if __name__ == '__main__':
    unittest.main()