import math
import task1.main
import scipy
A = 0
B = 1

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

for N in range(1, 8):
    print(f"{N}--------------------")
    roots = get_lezandr_roots(N)
    print(roots)
    C = [get_cK(N, i, roots) for i in range(0, N)]
    print(sum(C))
    integral = 0
    l = (B-A)/2
    for i in range(len(C)):
        integral += l * C[i]*f(l*roots[i] + l + A)
    print(integral)
    math_res = scipy.integrate.quad(f, A, B)
    print(f'Невязка: {abs(math_res[0])}')