import math
import scipy
import numpy


def p(x):
    return -1 * math.log(x, math.e)


def f(x):
    return math.sin(x)


def foo(x):
    return p(x) * f(x)


def polynom(x, n):
    res = 0
    for i in range(n):
        res += x**i
    return res


def pol_int(x, n):
    return polynom(x, n) * p(x)


def main():
    a = float(input('Введите нижний предел интегрирования: '))
    b = float(input('Введите верхний предел интегрирования: '))

    while a >= b:
        print('Значение левого конца должно быть меньше правого. Введите корректные данные ')
        a = float(input('Введите нижний предел интегрирования: '))
        b = float(input('Введите верхний предел интегрирования: '))
    math_res = scipy.integrate.quad(foo, a, b)
    print('"Точное" значение интеграла: ', f'{math_res[0]} с точностью {math_res[1]}')

    n = int(input('ВВедите количество узлов для ИКФ: '))
    nodes = []
    h = (b - a) / n
    for i in range(n):
        nodes.append(a + h * i)

    m = []
    for i in range(n):
        def func(x):
            return p(x) * x**i
        cur = scipy.integrate.quad(func, a, b)
        m.append(cur[0])
        print(f"m_{i} = {m[i]}")

    matr = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(nodes[j] ** i)
        matr.append(line)
    A = numpy.array(matr)
    B = numpy.array(m)
    X = numpy.linalg.solve(A, B)
    for i in range(n):
        print(f"A_{i} = {X[i]}")

    res = 0
    for i in range(n):
        res += X[i] * f(nodes[i])

    print(f"Вычисленное значение интеграка по ИКФ с {n} узлами равна {res}")
    print(f"Погрешность равна {abs(math_res[0] - res)}")

    print(f"Проверка ИКФ на точность: подставим полином степени {n}")

    def func(x):
        return pol_int(x, n)
    math_res_pol = scipy.integrate.quad(func, a, b)
    print('"Точное" значение интеграла: ', f'{math_res_pol[0]} с точностью {math_res_pol[1]}')

    res_pol = 0
    for i in range(n):
        res_pol += X[i] * polynom(nodes[i], n)
    print(f"Вычисленное значение интеграка по ИКФ с {n} узлами равна {res_pol}")
    print(f"Погрешность равна {abs(math_res_pol[0] - res_pol)}")

print(
    '"Приближённое вычисление интегралов при помощи квадратурных формул\nНаивысшей Алгебраической Степени Точности '
    '(КФ НАСТ)"\nВариант 5\nВыполнили Житнухина Мария и Карасева Елизавета')

main()