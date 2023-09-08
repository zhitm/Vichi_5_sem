import math

A = -10
e = 10 ** (-7)
B = 2

def f(x):
   return x * math.sin(x) - 1


def f_derr(x):
    return x * math.cos(x) + math.sin(x)


def has_root(a, b):
    return (f(a) > 0 > f(b)) or (f(a) < 0 < f(b)) or f(a) == 0 or f(b) == 0
    # я не помню, что если выпал корень


def root_separation(n_parts):
    part_len = (B - A) / N
    current_point = A
    good_segms = []
    for i in range(n_parts):
        if has_root(current_point, current_point + part_len):
            good_segms.append([current_point, current_point + part_len])
        current_point += part_len
    return good_segms


def print_info():
    print('''
    Численные методы решения нелинейных уравнений
    Работа выполнена Житнухиной Марией и Карасевой Елизаветой, группа 21.Б10
    Отрезок: [-10, 2]
    Функция: x*sin(x)-1
    Точность: ε = 10^(-7)
    ''')


def bisection(segm):
    a, b = segm[0], segm[1]
    while True:
        c = (a + b) / 2
        if has_root(a, b):
            b = c
        else:
            a = c
        if (b - a) <= 2 * e:
            X = (a+b)/2
            delta = (b-a)/2

            return X, delta


def secant_method(segm):
    a, b = segm[0], segm[1]
    while abs(f(b))>e:
        b = b - f(b)/(f(b)-f(a))*(b-a)
    return b

print_info()
N = int(input("Введите количество делений отрезка: "))

good_segms = root_separation(N)

print("Метод бисекции")
for segm in good_segms:
    X, delta = bisection(segm)
    print(segm)
    print(f'Корень: {X}, абсолютная погрешность: {abs(f(X))}')

print("Метод секущих")
for segm in good_segms:
    X = secant_method(segm)
    print(segm)
    print(f'Корень: {X}, абсолютная погрешность: {abs(f(X))}')
