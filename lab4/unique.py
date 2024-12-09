# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.elem = set()
        self.data = items
        self.index = 0
        self.ignore_case = kwargs.get('ignore_case', False)  # меняем true-false местами

    def __next__(self):
        while self.index < len(self.data):
            item = self.data[self.index]
            item = item.lower() if self.ignore_case else item
            if item not in self.elem:
                self.elem.add(item)
                return item

            self.index += 1

        raise StopIteration()  # Завершаем итерацию, если все элементы обработаны

    def __iter__(self):
        return self


if __name__ == "__main__":
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    unique_iterator = Unique(data)
    print(list(unique_iterator))  # Вывод: [1, 2]

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    unique_iterator = Unique(data, ignore_case=True)
    print(list(unique_iterator))  # Вывод: ['a', 'b']
