import math

A = -10
e = 10 ** (-7)
B = 2


def f(x):
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


def has_root(a, b):
    """
    Check if function has at least one root on the segment
    :param a: left boarder of the segment
    :param b: right boarder of the segment
    :return: the fact of the presence of a root
    """
    return (f(a) > 0 > f(b)) or (f(a) < 0 < f(b)) or f(a) == 0 or f(b) == 0
    # я не помню, что если выпал корень


def root_separation(n_parts):
    """
    Root separation process
    :param n_parts: the number of parts into which we divide the segment
    :return: list of segments containing roots
    """
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
    while counter < 40:
        c = (a + b) / 2
        if has_root(a, b):
            b = c
        else:
            a = c
        approaching.append(c)
        counter += 1
        if (b - a) <= 2 * e:
            break
    X = (a + b) / 2
    delta = (b - a) / 2
    return approaching, X, delta


def secant_method(segm):
    """
    Finding the roots of an equation using the secant method
    :param segm: segment with roots
    :return: root
    """
    a, b = segm[0], segm[1]
    counter = 0
    approaching = [b]
    while abs(f(b)) > e and counter < 20:
        b = b - f(b) / (f(b) - f(a)) * (b - a)
        approaching.append(b)
        counter += 1
    return approaching, b


def check_convergence(x0):
    return f(x0) * f_sec_derr(x0) > 0


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
    while abs(f(b)) > e and counter < 20:
        b = b - f(b) / f_derr(b)
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
    while abs(f(b)) > e and counter < 20:
        b = b - f(b) / f_derr(x0)
        approaching.append(b)
        counter += 1
    return approaching, b


print_info()
N = int(input("Введите количество делений отрезка: "))

good_segms = root_separation(N)
print(f"Количество отрезков, содержащих корни: {len(good_segms)}")

print("\nМетод бисекции")
for segm in good_segms:
    app, X, delta = bisection(segm)
    print(segm)
    print(f'''Количество шагов: {len(app)}, приближения: {*app,}''')
    print(f'Корень: {X}, длина последнего отрезка: {delta}, абсолютная погрешность: {abs(f(X))}')

print("\nМетод секущих")
for segm in good_segms:
    app, X = secant_method(segm)
    print(segm)
    print(f'''Количество шагов: {len(app)}, приближения: {*app,}''')
    print(f'Корень: {X}, разность последних приближений: {abs(app[-2] - app[-1])}, абсолютная погрешность: {abs(f(X))}')

print("\nМетод касательных")
for segm in good_segms:
    app, X, is_conv = tangent_method(segm)
    print(segm)
    print(f'''Количество шагов: {len(app)}, приближения: {*app,}''')
    print(f'Корень: {X}, разность последних приближений: {abs(app[-2] - app[-1])}, абсолютная погрешность: {abs(f(X))},'
          f' ряд {"сходится" if is_conv else "не сходится"}')

print("\nМодифицированный метод Ньютона")
for segm in good_segms:
    app, X = modify_newton_method(segm)
    print(segm)
    print(f'''Количество шагов: {len(app)}, приближения: {*app,}''')
    print(f'Корень: {X}, разность последних приближений: {abs(app[-2] - app[-1])}, абсолютная погрешность: {abs(f(X))}')
