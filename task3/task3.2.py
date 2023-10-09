import math

import pandas as pandas


def f(x):
    """
    Заданная функция
    :param x: Переменная
    :return: Значение функции
    """
    return math.exp(1.5 * x)


def real_first_derr(x):
    """
    Заданная функция
    :param x: Переменная
    :return: Значение первой прозводной функции
    """
    return f(x) * 1.5


def real_second_derr(x):
    """
    Заданная функция
    :param x: Переменная
    :return: Значение второй прозводной функции
    """
    return f(x) * 1.5 * 1.5


def calc_second_derr(values, i, h):
    """
       Заданная функция
       :param values: Значения в узлах
       :param i: Индекс узла
       :param h: Расстояние между соседники узлами
       :return: Значение второй прозводной функции (численный метод)
       """
    return (values[i + 1] - 2 * values[i] + values[i - 1]) / (h * h)


def calc_first_derr(values, i, h):
    """
    Заданная функция
    :param values: Значения в узлах
    :param i: Индекс узла
    :param h: Расстояние между соседники узлами
    :return: Значение первой прозводной функции (численный метод)
    """
    if i == 0:
        return (-3 * values[0] + 4 * values[1] - values[2]) / h
    if i == len(values) - 1:
        return (values[i] - 4 * values[i - 1] + values[i - 2]) / (2 * h)
    return (values[i + 1] - values[i]) / (2 * h)


def main():
    m = int(input('Введите число значений в таблице: '))
    while m <= 1:
        m = int(input('Введите число, большее 1! '))

    a = float(input('Введите значений левого конца отрезка: '))
    h = float(input('Введите значение шага h: '))
    while h < 0:
        h = float(input('Введите положительное значение шага h: '))

    nodes = [a + j * h for j in range(m)]
    values = [f(node) for node in nodes]
    print('Сформированная таблица значений функции:')
    print(pandas.DataFrame({'f(x_i)': values, 'x_i': nodes}))

    my_fst_derr = [calc_first_derr(values, i, h) for i in range(m)]
    my_scnd_derr = [None] + [calc_second_derr(values, i, h) for i in range(1, m - 1)] + [None]
    real_fst_derr = [real_first_derr(x) for x in nodes]
    abs_fst_derr = [abs(my_fst_derr[i] - real_fst_derr[i]) for i in range(m)]
    real_scnd_derr = [real_second_derr(x) for x in nodes]
    abs_scnd_derr = [None] + [abs(my_scnd_derr[i] - real_scnd_derr[i]) for i in range(1, m - 1)] + [None]

    pandas.set_option('display.max_columns', 500)

    print(pandas.DataFrame(
        {'x_i': nodes, 'f(x_i)': values, 'f\'(x_i) чд': my_fst_derr, '|f\'(x_i) чд - f\'(x_i)|': abs_fst_derr,
         'f\'\'(x_i) чд': my_scnd_derr, '|f\'\'(x_i) чд - f\'\'(x_i)|': abs_scnd_derr}))

    choice = input('Если хотите выйти из программы, введите любой символ кроме 1. Иначе введите 1, чтобы продолжить: ')
    if choice == '1':
        main()


print('Нахождение производных таблично-заданной функции по формулам численного дифференцирования\n'
      'Выполнили Житнухина Мария и Карасева Елизавета, 21.Б10-мм\nВариант 5')
main()
