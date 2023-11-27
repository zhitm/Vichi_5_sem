import math
import task1.main
import scipy
a = 0
b = 1


def f(x):
    return math.log(1+x, math.e)/(1+x**2)


def lezandr(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return (2*n-1)/n * lezandr(x, n-1)*x - (n-1)/n * lezandr(x, n-2)


def get_lezandr_roots(n):
    def func(x):
        return lezandr(x, n)
    parts = 1000
    good_segms = task1.main.root_separation(-1, 1, parts, func)
    roots = []
    for s in good_segms:
        _, X = task1.main.secant_method(s, func)
        roots.append(X)
    return roots


def get_cK(n, k, roots):
    return 2*(1-roots[k]**2)/n**2/(lezandr(roots[k], n-1)**2)


def polynom(x, n):
    res = 0
    for i in range(2*n - 1):
        res += x ** i
    return res


def check_polynom(n, roots, c):
    def func(x):
        return polynom(x, n)

    print(f"Проверка ИКФ на точность: подставим полином степени {2*n - 1}")
    res_pol = 0
    for i in\
            range(n):
        res_pol += c[i] * polynom(roots[i], n)
    print(f"Вычисленное значение интеграла по ИКФ с {2*n-1} узлами равна {res_pol}")
    math_res_pol = scipy.integrate.quad(func, -1, 1)
    print('"Точное" значение интеграла: ', f'{math_res_pol[0]} с точностью {math_res_pol[1]}')
    print(f"Погрешность равна {abs(math_res_pol[0] - res_pol)}")


def nodes_koefs(n):
    print(f"\nКоличество узлов N = {n}")
    roots = get_lezandr_roots(n)
    print("           Узлы               Коэффициенты КФ Гаусса")
    C = [get_cK(n, i, roots) for i in range(0, n)]
    for i in range(n):
        print(f"x_{i} = {roots[i]}\t a_{i} = {C[i]}")
    print(f"Проверка: сумма коэффициентов = {sum(C)}")
    return roots, C


def integrate_kf(n):
    roots, C = nodes_koefs(n)
    integral = 0
    l = (b - a) / 2
    for i in range(len(C)):
        integral += l * C[i] * f(l * roots[i] + l + a)
    print(f"Вычисленное значение интеграла с {n} узлами = {integral}")
    math_res = scipy.integrate.quad(f, a, b)
    print(f"Точное значение интеграла с {n} узлами = {math_res[0]}")
    print(f'Невязка: {abs(integral - math_res[0])}')


def main():
    for N in range(1, 8):
        roots, c = nodes_koefs(N)
        if N == 3 or N == 4 or N == 5:
            check_polynom(N, roots, c)

    s = input("Введите число узлов для вычисления интеграла. Чтобы выйти, введите 'quit'\n> ")
    while s != 'quit':
        nodes = int(s)
        integrate_kf(nodes)
        s = input("Введите число узлов для вычисления интеграла. Чтобы выйти, введите 'quit'\n> ")



print("КФ Гаусса, ее узлы и коэффициенты\nВычисление интегралов при помощи КФ Гаусса\nВариант 5\nВыполнили "
      "Житнухина Мария и Карасева Елизавета")
a = int(input("Введите границы отрезка\nа = "))
b = int(input("b = "))

while a >= b:
    print("Левая граница должна быть меньше правой. Введите корректные данные.")
    a = int(input("а = "))
    b = int(input("b = "))

main()
