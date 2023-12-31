import math

A = -10
e = 10 ** (-12)
B = 2


def fun(x):
    """
    Example of function to solve
    :param x: variable
    :return: function value
    """
    return x * math.sin(x) - 1


def f_derr(x):
    return x * math.cos(x) + math.sin(x)


def f_sec_derr(x):
    return 2 * math.cos(x) - x * math.sin(x)


def has_root(a, b, f):
    """
    Check if function has at least one root on the segment
    :param a: left boarder of the segment
    :param b: right boarder of the segment
    :return: the fact of the presence of a root
    """
    return (f(a) > 0 > f(b)) or (f(a) < 0 < f(b)) or f(a) == 0 or f(b) == 0


def root_separation(A, B, n_parts, f):
    """
    Root separation process
    :param n_parts: the number of parts into which we divide the segment
    :return: list of segments containing roots
    """
    part_len = (B - A) / n_parts
    current_point = A
    good_segms = []
    for i in range(n_parts):
        if has_root(current_point, current_point + part_len, f):
            good_segms.append([current_point, current_point + part_len])
        current_point += part_len
    return good_segms


def print_info():
    print('''
    Численные методы решения нелинейных уравнений
    Работа выполнена Житнухиной Марией и Карасевой Елизаветой, группа 21.Б10-мм
    Отрезок: [-10, 2]
    Функция: x*sin(x)-1
    Точность: ε = 10^(-7)
    ''')


def bisection(segm):
    """
    Finding the roots of an equation using the bisection method
    :param segm: segment with roots
    :return: root and measurement error
    """
    a, b = segm[0], segm[1]
    counter = 0
    approaching = [b]
    while counter < 100:
        c = (a + b) / 2
        if has_root(a, c, fun):
            b = c
        else:
            a = c
        approaching.append(c)
        counter += 1
        if (b - a) <= 2 * e:
            break
    X = (a+b)/2
    delta = (b - a) / 2
    return approaching, X, delta


def secant_method(segm, f):
    """
    Finding the roots of an equation using the secant method
    :param segm: segment with roots
    :return: root
    """
    a, b = segm[0], segm[1]
    counter = 0
    approaching = [b]
    while abs(f(b)) > e and counter < 50:
        null_cnt = 0
        while f(a) == f(b) and null_cnt < 20:
            null_cnt += 1
            a -= e / 40
        if f(a) == f(b):
            print("Деление на 0")
            return approaching, None
        b = b - f(b) / (f(b) - f(a)) * (b - a)
        approaching.append(b)
        counter += 1
    return approaching, b


def check_convergence(x0):
    return fun(x0) * f_sec_derr(x0) > 0


def tangent_method(segm):
    """
    Finding the roots of an equation using the tangent method
    :param segm: segment with roots
    :return: root
    """
    a, b = segm[0], segm[1]
    x0 = (a + b) / 2
    counter = 0
    approaching = [b]
    while abs(fun(b)) > e and counter < 40:
        null_cnt = 0
        while f_derr(b) == 0 and null_cnt < 20:
            null_cnt += 1
            b -= e / 20
        if f_derr(b) == 0:
            print("Деление на 0.")
            return approaching, None
        b = b - fun(b) / f_derr(b)
        approaching.append(b)
        counter += 1
    return approaching, b, check_convergence(x0)


def modify_newton_method(segm):
    """
    Finding the roots of an equation using the tangent method
    :param segm: segment with roots
    :return: root
    """
    a, b = segm[0], segm[1]
    x0 = (a + b) / 2
    counter = 0
    approaching = [b]
    while abs(fun(b)) > e and counter < 20:
        null_cnt = 0
        while f_derr(x0) == 0 and null_cnt < 40:
            null_cnt += 1
            x0 -= e / 20
        if f_derr(x0) == 0:
            print("Деление на 0.")
            return approaching, None
        b = b - fun(b) / f_derr(x0)
        approaching.append(b)
        counter += 1
    return approaching, b


# print_info()
# N = int(input("Введите количество делений отрезка: "))
#
# good_segms = root_separation(A, B, N, f)
# print(f"Количество отрезков, содержащих корни: {len(good_segms)}")


# print("\nМетод бисекции")
# for segm in good_segms:
#     app, X, delta = bisection(segm)
#     print(segm)
#     print(f'''Количество шагов: {len(app)}, приближения: {*app,}''')
#     print(f'Корень: {X}, длина последнего отрезка: {delta}, абсолютная погрешность: {abs(f(X))}')
#
# print("\nМетод секущих")
# for segm in good_segms:
#     app, X = secant_method(segm)
#     print(segm)
#     print(f'''Количество шагов: {len(app)}, приближения: {*app,}''')
#     print(f'Корень: {X}, разность последних приближений: {abs(app[-2] - app[-1])}, абсолютная погрешность: {abs(f(X))}')
#
# print("\nМетод касательных")
# for segm in good_segms:
#     app, X, is_conv = tangent_method(segm)
#     print(segm)
#     print(f'''Количество шагов: {len(app)}, приближения: {*app,}''')
#     print(f'Корень: {X}, разность последних приближений: {abs(app[-2] - app[-1])}, абсолютная погрешность: {abs(f(X))},'
#           f' ряд {"сходится" if is_conv else "не сходится"}')
#
# print("\nМодифицированный метод Ньютона")
# for segm in good_segms:
#     app, X = modify_newton_method(segm)
#     print(segm)
#     print(f'''Количество шагов: {len(app)}, приближения: {*app,}''')
#     print(f'Корень: {X}, разность последних приближений: {abs(app[-2] - app[-1])}, абсолютная погрешность: {abs(f(X))}')


# for segm in good_segms:
#     app, X, delta = bisection(segm)
#     print(f'Отрезок: {segm}')
#     print('Метод бисекции:')
#     print(f'''Количество шагов: {len(app)}, приближения: {*app,}''')
#     print(f'Корень: {X}, длина последнего отрезка: {delta}, невязка: {abs(f(X))}')
#
#     print("\nМетод секущих")
#     app, X = secant_method(segm, f)
#     print(f'''Количество шагов: {len(app)}, приближения: {*app,}''')
#     print(f'Корень: {X}, разность последних приближений: {abs(app[-2] - app[-1])}, невязка: {abs(f(X))}')
#
#     print("\nМетод касательных")
#     app, X, is_conv = tangent_method(segm)
#     print(f'''Количество шагов: {len(app)}, приближения: {*app,}''')
#     print(f'Корень: {X}, разность последних приближений: {abs(app[-2] - app[-1])}, невязка: {abs(f(X))},'
#           f' ряд {"сходится" if is_conv else "не сходится"}')
#
#     print("\nМодифицированный метод Ньютона")
#     app, X = modify_newton_method(segm)
#     print(f'''Количество шагов: {len(app)}, приближения: {*app,}''')
#     print(f'Корень: {X}, разность последних приближений: {abs(app[-2] - app[-1])}, невязка: {abs(f(X))}')
#
#     print('-------------------------------------------------------')
