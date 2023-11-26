import math
import scipy
import numpy


def p(x):
    if x == 0:
        return 0
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


def get_moment(k, a, b):
    def moment_func(x):
        return x**k*p(x)
    return scipy.integrate.quad(moment_func, a, b)[0]


def get_ortogonal_koefs(n, a, b):
    moments = []
    for i in range(2*n):
        moments.append(get_moment(i, a, b))

    table = []
    for i in range(n):
        row = moments[i:i+n]
        table.append(row)
    A = numpy.array(table)
    B = numpy.array(moments[n:2*n+1])

    koefs = numpy.linalg.solve(A, (-1) * B)
    print("Ортогональные коэффициенты:")
    for i in range(n):
        print(f"a_{i} = {koefs[i]}")
    return numpy.linalg.solve(A, (-1)*B)


def get_roots(n, a, b):
    koefs = numpy.insert(numpy.flip(get_ortogonal_koefs(n, a, b)), 0, 1)
    roots = numpy.flip(numpy.roots(koefs))
    print("Найденные корни:")
    for i in range(n):
        print(f"x_{i} = {roots[i]}")
    return roots


def calculate_value(func, coefs, nodes):
    result = 0
    for i in range(len(nodes)):
        result += coefs[i] * func(nodes[i])
    return result


def get_ikf(a, b, nodes):
    n = len(nodes)
    m = []
    print("Моменты (из построения КФ):")
    for i in range(n):
        def func(x):
            return p(x) * x ** i

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
    print("Коэффициенты КФ:")
    for i in range(n):
        print(f"A_{i} = {X[i]}")
    res = 0
    for i in range(n):
        res += X[i] * f(nodes[i])

    return X, res


def main():
    a = float(input('Введите нижний предел интегрирования: '))
    b = float(input('Введите верхний предел интегрирования: '))

    while a >= b:
        print('Значение левого конца должно быть меньше правого. Введите корректные данные ')
        a = float(input('Введите нижний предел интегрирования: '))
        b = float(input('Введите верхний предел интегрирования: '))

    n = int(input('Введите количество узлов для ИКФ: '))

    nodes = []
    h = (b - a) / n
    print(f"Узлы ИКФ с АСТ = {n}:")
    for i in range(n):
        nodes.append(a + h * i)
        print(f"x_{i} = {nodes[i]}")
    X, res = get_ikf(a, b, nodes)

    math_res = scipy.integrate.quad(foo, a, b)
    print('"Точное" значение интеграла: ', f'{math_res[0]} с точностью {math_res[1]}')
    print(f"Вычисленное значение интеграла по ИКФ с {n} узлами равна {res}")
    print(f"Погрешность равна {abs(math_res[0] - res)}")

    print(f"Проверка ИКФ на точность: подставим полином степени {n - 1}")

    def func(x):
        return pol_int(x, n)
    math_res_pol = scipy.integrate.quad(func, a, b)
    print('"Точное" значение интеграла: ', f'{math_res_pol[0]} с точностью {math_res_pol[1]}')


    res_pol = 0
    for i in range(n):
        res_pol += X[i] * polynom(nodes[i], n)

    print(f"Вычисленное значение интеграла по ИКФ с {n} узлами равна {res_pol}")
    print(f"Погрешность равна {abs(math_res_pol[0] - res_pol)}")

    kfnast_nodes = get_roots(n, a, b)
    x, res_kfnast = get_ikf(a, b, kfnast_nodes)
    res = 0

    def fun(x):
        return x**(2*n-1)

    def fun_p(x):
        return fun(x)*p(x)
    res = calculate_value(fun, x, kfnast_nodes)
    math_res = scipy.integrate.quad(fun_p, a, b)
    print(f"Вычисленное значение интеграла по КФНАСТ с {len(kfnast_nodes)} узлами для одночлена степени {2*n - 1} равна {res}")
    print(f"Точное значение: {math_res[0]}")
    print(f"Погрешность равна {abs(math_res[0] - res)}")



print(
    '"Приближённое вычисление интегралов при помощи квадратурных формул\nНаивысшей Алгебраической Степени Точности '
    '(КФ НАСТ)"\nВариант 5\nВыполнили Житнухина Мария и Карасева Елизавета')

main()