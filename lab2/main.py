from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import requests


def main():

    rect = Rectangle("синего" ,18,18)
    circ = Circle("зеленого", 18)
    sqr = Square("красного", 18)
    print(rect)
    print(circ)
    print(sqr)
    #response = requests.get('https://sky.pro/media/')
    #print(response.ok)  # проверяем успешен ли запрос?


if __name__ == "__main__":
    main()