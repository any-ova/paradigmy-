# Здесь должна быть реализация декоратора
# Исправленная реализация декоратора
def print_result(func):
    def wrapper(*args, **kwargs):  # Принимаем произвольные аргументы
        print("Функция:", func.__name__)
        res = func(*args, **kwargs)  # Передаем аргументы в оригинальную функцию
        if isinstance(res, list):
            for i in res:
                print(i)
        elif isinstance(res, dict):
            for i, j in res.items():
                print(i, "=", j)
        else:
            print(res)
        return res
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
