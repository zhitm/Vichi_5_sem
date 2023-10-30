import pandas as pandas


def int_f(a, b):
    return (b*b-a*a)/2


def f(x):
    return x


def kf_left_triangle(f, a, b):
    return (b - a) * f(a)


def kf_right_triangle(f, a, b):
    return (b - a) * f(b)


def kf_middle_triangle(f, a, b):
    return (b - a) * f((a + b) / 2)


def kf_trapezoid(f, a, b):
    return (b - a) / 2 * (f(a) + f(b))


def kf_simpson(f, a, b):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))


def kf_3_8(f, a, b):
    h = (b - a) / 3
    return (b - a) * (1 / 8 * f(a) + 3 / 8 * f(a + h) + 3 / 8 * f(a + 2 * h) + 1 / 8 * f(b))


def main():
    a = float(input('Введите значений левого конца отрезка: '))
    b = float(input('Введите значений правого конца отрезка: '))

    while a >= b:
        print('Значение левого конца должно быть меньше правого. Введите корректные данные ')
        a = float(input('Введите значений левого конца отрезка: '))
        b = float(input('Введите значений правого конца отрезка: '))

    kflt = kf_left_triangle(f, a, b)
    kfrt = kf_right_triangle(f, a, b)
    kfmt = kf_middle_triangle(f, a, b)
    kft = kf_trapezoid(f, a, b)
    kfs = kf_simpson(f, a, b)
    kf38 = kf_3_8(f, a, b)
    integrals = [kflt, kfrt, kfmt, kft, kfs, kf38]
    real_value = int_f(a, b)
    print(f'Точное значение интеграла: {real_value}')
    abses = [abs(real_value - kflt), abs(real_value - kfrt), abs(real_value - kfmt), abs(real_value - kft),
             abs(real_value - kfs), abs(real_value - kf38)]
    methods = ['КФ левого прямоугольника', 'КФ правого прямоугольника', 'КФ среднего прямоугольника', 'КФ трапеции', 'КФ Симпсона']
    table = pandas.DataFrame({'Вычисленные значения': integrals, 'Погрешность': abses})
    table.index = methods
    print(table)

print('Приближенное вычисление интеграла по приближенным формулам\nВариант 5\nВыполнили Житнухина Мария и Карасева Елизавета')

main()
