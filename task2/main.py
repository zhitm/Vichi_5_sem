import pandas
import math
import random


def f(x):
    """
    Заданная функция
    :param x: Переменная
    :return: Значение функции
    """
    return 1 - math.exp(-2 * x)


def create_table(m, a, b, choice):
    """
    Создание таблицы значений функции f(x)
    :param m: Количество значений в таблице
    :param a: Левая граница отрезка
    :param b: Правая граница отрезка
    :param choice: Выбор построения - случайные или равномерно распределенные точки
    :return: Таблица и список точек
    """
    if choice == 1:
        nodes = []
        while len(nodes) <= m:
            el = random.uniform(a, b)
            if el not in nodes:
                nodes.append(el)
    else:
        h = (b - a) / m
        nodes = [a + j * h for j in range(m + 1)]
    return nodes


def lagrange_interpolation(x, nodes):
    """
    Значение интерполяционного многочлена, найденное при помощи представления в форме Лагранжа
    :param x: Переменная
    :param nodes: Список точек, где будем искать значения
    :return: Значение функции
    """
    if abs(nodes[0] - x) < 1E-6:
        return f(nodes[0])

    result = 0
    for j in range(len(nodes)):
        term = f(nodes[j])
        for i in range(len(nodes)):
            if i != j:
                term *= (x - nodes[i]) / (nodes[j] - nodes[i])
        result += term
    return result


def main():
    print('Задача алгебраического интерполирования\n Вариант 5')

    print('Введите число значений в таблице: ')
    m = int(input()) - 1

    print('Введите значений концов отрезка: ')
    a = float(input())
    b = float(input())
    while a >= b:
        print('Значение левого конца должно быть меньше правого. Введите корректные данные: ')
        a = float(input())
        b = float(input())

    print('Если хотите таблицу со случайными узлами - напишите 1, иначе - 2:')
    choice = int(input())
    while choice != 1 and choice != 2:
        print('Некорректная команда. Введите число 1 или 2: ')
        choice = int(input())

    nodes = create_table(m, a, b, choice)
    print('Сформированная таблица значений функции:')
    print(pandas.DataFrame({'z_j': nodes, 'f(z_j)': [f(node) for node in nodes]}))

    print('Введите точку X интерполирования: ')
    x = float(input())

    print(f'Введите степень интерполяционного многочлена, не выше {m}')
    n = int(input())
    while n > m:
        print(f'Введено недопустимое значение n. Введите число, меньшее {m}')

    selected_nodes = sorted(nodes, key=lambda z: abs(z - x))[:n + 1]
    print('Набор узлов, ближайших к точке Х:')
    print(pandas.DataFrame({'z_j': selected_nodes, 'f(z_j)': [f(node) for node in selected_nodes]}))

    lagrange = lagrange_interpolation(x, selected_nodes)
    print(f'Значение по Лагранжу: {lagrange}')
    print(f'Абсолютная фактическая погрешность для формы Лагранжа: {abs(lagrange - f(x))}')


main()
