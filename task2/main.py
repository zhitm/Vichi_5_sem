import pandas
import math
import random


def f(x):
    """
    Заданная функция
    :param x: Переменная
    :return: Значение функции
    """
    # return 1 - math.exp(-2 * x)
    return x**2*(x-0.18)*(x+1.2)-3.5


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
    :param nodes: Список точек, где известно значение
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


def newton_method(x, nodes):
    """
    Значение интерполяционного многочлена, найденное при помощи представления в форме Ньютона
    :param x: Переменная
    :param nodes: Список точек, где известно значение
    :return: Значение функции
    """
    table = [nodes, [f(el) for el in nodes]]
    l = len(nodes)
    # создаем таблицу разделенных разностей
    for i in range(2, l + 1):
        col = []
        last_col = table[-1]
        last_col_len = len(last_col)
        for ind in range(last_col_len - 1):
            col.append((last_col[ind + 1] - last_col[ind]) / (nodes[ind + i - 1] - nodes[ind]))
        table.append(col)

    print("Таблица разделенных разностей:")
    for el in table:
        print(el)

    coefs = [table[i][0] for i in range(1, len(table))]
    # вычисляю значение
    p = coefs[0]
    acc = 1
    for i in range(1, l):
        acc *= x - nodes[0]
        p += coefs[i] * acc
    return p


def main():
    x = float(input('Введите точку X интерполирования: '))

    n = int(input(f'Введите степень интерполяционного многочлена, не выше {m}: '))
    while n > m or n < 0:
        n = int(input(f'Введено недопустимое значение n. Введите положительное число, меньшее {m}: '))

    selected_nodes = sorted(nodes, key=lambda z: abs(z - x))[:n + 1]
    print('Набор узлов, ближайших к точке Х:')
    print(pandas.DataFrame({'z_j': selected_nodes, 'f(z_j)': [f(node) for node in selected_nodes]}))

    lagrange = lagrange_interpolation(x, selected_nodes)
    print(f'Значение по Лагранжу: {lagrange}')
    print(f'Абсолютная фактическая погрешность для формы Лагранжа: {abs(lagrange - f(x))}')

    newton = newton_method(x, selected_nodes)
    print(f'Значение по Ньютону: {newton}')
    print(f'Абсолютная фактическая погрешность для многочлена Ньютона: {abs(newton - f(x))}')

    str = input('Если хотите выйти из программы, введите любой символ кроме 1. Иначе введите 1, чтобы продолжить: ')
    if str == '1':
        main()


print('Задача алгебраического интерполирования\nВыполнили Житнухина Мария и Карасева Елизавета, 21.Б10-мм\nВариант 5')

m = int(input('Введите число значений в таблице: ')) - 1
while m <= 0:
    m = int(input('Введите число, большее 1! ')) - 1

a = float(input('Введите значение левого конца отрезка: '))
b = float(input('Введите значение правого конца отрезка: '))
while a >= b:
    print('Значение левого конца должно быть меньше правого. Введите корректные данные ')
    a = float(input('Введите значение левого конца отрезка: '))
    b = float(input('Введите значение правого конца отрезка: '))

print('Если хотите таблицу со случайными узлами - напишите 1, иначе - 2:')
choice = int(input())
while choice != 1 and choice != 2:
    print('Некорректная команда. Введите число 1 или 2: ')
    choice = int(input())

nodes = create_table(m, a, b, choice)
print('Сформированная таблица значений функции:')
print(pandas.DataFrame({'z_j': nodes, 'f(z_j)': [f(node) for node in nodes]}))

main()
