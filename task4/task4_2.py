import pandas as pandas
import math


def p(x):
    return 1


# def f(x):
#  return x
#
#
# def int_f(a, b):
#  return (b * b - a * a) / 2



def int_f(a, b):
    return (b*b-a*a)/2-math.cos(b)+math.cos(a)


def f(x):
    return x+math.sin(x)


def foo(x):
    return f(x) * p(x)


def s_kf_left_triangle(f, a, b, m):
    h = (b - a) / m
    res = 0
    for i in range(m):
        res += f(a + i * h)
    return h * res


def s_kf_right_triangle(f, a, b, m):
    h = (b - a) / m
    res = 0
    for i in range(m):
        res += f(a + (i + 1) * h)
    return h * res


def s_kf_middle_triangle(f, a, b, m):
    x1 = 1 / 2
    h = (b - a) / m
    res = 0
    for i in range(m):
        res += f(a + (i + x1) * h)
    return h * res


def s_kf_trapezoid(f, a, b, m):
    h = (b - a) / m
    res = f(a) + f(b)
    for i in range(1, m):
        res += 2 * f(a + i * h)
    return h / 2 * res


def s_kf_simpson(f, a, b, m):
    h = (b - a) / m
    res = 0
    for i in range(m):
        res += f(a + i * h) + 4 * f(a + h * (i + 1 / 2)) + f(a + (i + 1) * h)
    return h / 6 * res


def main():
    a = float(input('Введите значение левого конца отрезка: '))
    b = float(input('Введите значение правого конца отрезка: '))

    while a >= b:
        print('Значение левого конца должно быть меньше правого. Введите корректные данные ')
        a = float(input('Введите значений левого конца отрезка: '))
        b = float(input('Введите значений правого конца отрезка: '))

    m = int(input(f'Введите число промежутков деления отрезков [{a}, {b}]: '))

    while m <= 0:
        print('Значение должно быть больше нуля. Введите корректные данные')
        m = int(input(f'Введите число промежутков деления отрезков [{a}, {b}]: '))

    kflt = s_kf_left_triangle(foo, a, b, m)
    kfrt = s_kf_right_triangle(foo, a, b, m)
    kfmt = s_kf_middle_triangle(foo, a, b, m)
    kft = s_kf_trapezoid(foo, a, b, m)
    kfs = s_kf_simpson(foo, a, b, m)
    integrals = [kflt, kfrt, kfmt, kft, kfs]
    real_value = int_f(a, b)
    print(f'Точное значение интеграла: {real_value}')

    abses = [abs(real_value - kflt), abs(real_value - kfrt), abs(real_value - kfmt), abs(real_value - kft),
             abs(real_value - kfs)]
    theor_abses = [(b - a) ** 2 / (2 * m), (b - a) ** 2 / (2 * m), 0, 0, 0]
    methods = ['СКФ левого прямоугольника', 'СКФ правого прямоугольника', 'СКФ среднего прямоугольника', 'СКФ трапеции',
               'СКФ Симпсона']
    table = pandas.DataFrame({'Вычисленные значения': integrals, 'Фактическая': abses, 'Теоретическая': theor_abses})
    table.index = methods
    print(table)


print(
    'Приближенное вычисление интеграла по составным квадратурным формулам\nВариант 5\nВыполнили Житнухина Мария и Карасева Елизавета')

main()
