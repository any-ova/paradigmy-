import json
import cm_timer
from print_result import print_result
from gen_random import gen_random
from unique import Unique

path = "C:/Users/annfr/PycharmProjects/lab4/data_light.json"


@print_result
def f1(arg):
    return sorted(Unique([vacancy['job-name'] for vacancy in arg], ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    salaries = list(gen_random(len(arg), 100000, 200000))
    result = [
        f"{specialty}, зарплата {salary} руб."
        for specialty, salary in zip(arg, salaries)
    ]
    return result


if __name__ == '__main__':
    with cm_timer.cm_timer_1():
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        f4(f3(f2(f1(data))))
