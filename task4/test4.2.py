import task4_2
import unittest


def const(x):
    return 10


def linear(x):
    return 2 * x + 1


def linear_int(a, b):
    return (b ** 2 + b - a - a ** 2)


def square(x):
    return 3 * x ** 2 + 2 * x - 3


def square_int(a, b):
    return (b ** 3 + b ** 2 - 3 * b - a ** 3 - a ** 2 + 3 * a)


def cube(x):
    return 4 * x ** 3 + 3 * x ** 2 + 2 * x + 10


def cube_int(a, b):
    return (b ** 4 + b ** 3 + b ** 2 + 10 * b - a ** 4 - a ** 3 - a ** 2 - 10 * a)


a = 2
b = 3
m = 200


class TestSum(unittest.TestCase):

    def test_left_tr(self):
        self.assertTrue(task4_2.s_kf_left_triangle(const, a, b, m) - 10 * (b - a) < 1e-8)

    def test_right_tr(self):
        self.assertTrue(task4_2.s_kf_right_triangle(const, a, b, m) - 10 * (b - a) < 1e-8)

    def test_middle_tr(self):
        self.assertTrue(task4_2.s_kf_middle_triangle(linear, a, b, m) - linear_int(a, b) < 1e-8)

    def test_trapezoid_tr(self):
        self.assertTrue(task4_2.s_kf_trapezoid(linear, a, b, m) - linear_int(a, b) < 1e-8)

    def test_simpson_tr(self):
        self.assertTrue(task4_2.s_kf_simpson(square, a, b, m) - square_int(a, b) < 1e-8)


if __name__ == '__main__':
    unittest.main()
