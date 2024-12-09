import math
import sys

def get_coef(index, prompt):
    try:
        # Try to read the coefficient from the command line
        coef_str = sys.argv[index]
    except:
        # Input from the keyboard
        print(prompt)
        coef_str = input()
    # check that numbers can be converted to float
    while True:
        try:
            coef = float(coef_str)
            return coef
        except ValueError:
            print('Invalid input. Please enter again:')
            coef_str = input()

def get_roots(a, b, c):
    '''
    Calculate the roots of a biquadratic equation
    Args:
        a (float): coefficient A
        b (float): coefficient B
        c (float): coefficient C
    '''
    result = set()
    D = b*b - 4*a*c
    if D >= 0.0:
        sqD = math.sqrt(D)
        temp_root1 = (-b + sqD) / (2.0 * a)
        temp_root2 = (-b - sqD) / (2.0 * a)
        if temp_root1 >= 0.0:
            root1 = math.sqrt(temp_root1)
            root2 = -1*math.sqrt(temp_root1)
            result.add(root1)
            result.add(root2)
        if temp_root2 >= 0.0:
            root3 = math.sqrt(temp_root2)
            root4 = -1*math.sqrt(temp_root2)
            result.add(root3)
            result.add(root4)
    return result

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    # Output the roots
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: ')
    elif len_roots == 2:
        print('Два корня: ')
    elif len_roots == 3:
        print('Три корня: ')
    elif len_roots == 4:
        print('Четыре корня: ')
    for root in roots:
        print(root)

if __name__ == '__main__':
    main()