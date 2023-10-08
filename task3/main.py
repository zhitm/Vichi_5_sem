import math

import pandas as pandas


e = 10 ** (-8)


def f(x):
    """
    Заданная функция
    :param x: Переменная
    :return: Значение функции
    """
    return 1 - math.exp(-2 * x)


def lagrange_interpolation(x, table):
    """
    Значение интерполяционного многочлена, найденное при помощи представления в форме Лагранжа
    :param x: Переменная
    :param table: Таблица значений функции
    :return: Значение функции в точке x
    """
    if abs(table[0][0] - x) < 1E-6:
        return table[1][0]

    result = 0
    for j in range(len(table[0])):
        term = table[1][j]
        for i in range(len(table[0])):
            if i != j:
                if abs(table[0][j] - table[0][i]) < e:
                    return None
                term *= (x - table[0][i]) / (table[0][j] - table[0][i])
        result += term
    return result


def has_root(a, b):
    """
    Check if function has at least one root on the segment
    :param a: left boarder of the segment
    :param b: right boarder of the segment
    :return: the fact of the presence of a root
    """
    return (f(a) > 0 > f(b)) or (f(a) < 0 < f(b)) or f(a) == 0 or f(b) == 0


def root_separation(n_parts, A, B):
    """
    Root separation process
    :param n_parts: the number of parts into which we divide the segment
    :return: list of segments containing roots
    """
    part_len = (B - A) / n_parts
    current_point = A
    good_segms = []
    for i in range(n_parts):
        if has_root(current_point, current_point + part_len):
            good_segms.append([current_point, current_point + part_len])
        current_point += part_len
    return good_segms


def secant_method(segm, F, table):
    """
    Finding the roots of an equation using the secant method
    :param segm: segment with roots
    :param F: value
    :param table: Values of function
    :return: root
    """
    a, b = segm[0], segm[1]
    counter = 0
    approaching = [b]
    while abs(lagrange_interpolation(b, table) - F) > e and counter < 50:
        null_cnt = 0
        while lagrange_interpolation(a, table) == lagrange_interpolation(b, table) and null_cnt < 20:
            null_cnt += 1
            a -= e / 40
        if lagrange_interpolation(a, table) == lagrange_interpolation(b, table):
            print("Деление на 0")
            return approaching, None
        b = b - (lagrange_interpolation(b, table) - F) / (lagrange_interpolation(b, table) -
                                                          lagrange_interpolation(a, table)) * (b - a)
        approaching.append(b)
        counter += 1
    return approaching, b


def main():
    print('Введите число значений в таблице: ')
    m = int(input()) - 1
    while m <= 0:
        m = int(input('Введите число, большее 1! ')) - 1

    a = float(input('Введите значений левого конца отрезка: '))
    b = float(input('Введите значений правого конца отрезка: '))

    h = (b - a) / m
    nodes = [a + j * h for j in range(m + 1)]
    print('Сформированная таблица значений функции:')
    print(pandas.DataFrame({'f(z_j)': [f(node) for node in nodes], 'f^-1(f(z_j))': nodes}))

    while a >= b:
        print('Значение левого конца должно быть меньше правого. Введите корректные данные ')
        a = float(input('Введите значений левого конца отрезка: '))
        b = float(input('Введите значений правого конца отрезка: '))

    print('Введите значение F, которое должна принимать функция: ')
    F = float(input())

    n = int(input(f'Введите степень интерполяционного многочлена, не выше {m}: '))
    while n > m:
        n = int(input(f'Введено недопустимое значение n. Введите число, меньшее {m}: '))

    print('I способ: интерполирование обратной функции')
    selected_nodes = sorted(nodes, key=lambda z: abs(f(z) - F))[:n + 1]
    print('Набор узлов, ближайших к значению F:')
    table = [[f(node) for node in selected_nodes], selected_nodes]
    print(pandas.DataFrame({'f(z_j)': table[0], 'f^-1(f(z_j))': table[1]}))

    lagrange = lagrange_interpolation(F, table)
    if lagrange:
        print(f'Аргумент функции f, при котором мы получаем значение {F} равен {lagrange}')
        print(f'Абсолютная фактическая погрешность для формы Лагранжа: {abs(F - f(lagrange))}')
    else:
        print('Функция не мотононная, метод Лагранжа не работает!')

    print('\nII способ: используем интерполяционный полином')
    table = [nodes, [f(node) for node in nodes]]
    good_segms = root_separation(n, a, b)

    print(f"Количество отрезков, содержащих корни: {len(good_segms)}")
    for segm in good_segms:
        app, X = secant_method(segm, F, table)
        print(f'Отрезок: {segm}, Корень: {X}, невязка: {abs(f(X) - F)}')

    print('Если хотите выйти из программы, введите любой символ кроме 1. Иначе введите 1, чтобы продолжить')
    choice = input()
    if choice == '1':
        main()


print('Задача обратного интерполирования\nВариант 5\nВыполнили Житнухина Мария и Карасева Елизавета')

main()
