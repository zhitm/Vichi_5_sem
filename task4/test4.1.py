import task4_1
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


class TestSum(unittest.TestCase):

    def test_left_tr(self):
        self.assertEqual(task4_1.kf_left_triangle(const, a, b), 10 * (b - a))

    def test_right_tr(self):
        self.assertEqual(task4_1.kf_right_triangle(const, a, b), 10 * (b - a))

    def test_middle_tr(self):
        self.assertEqual(task4_1.kf_middle_triangle(linear, a, b), linear_int(a, b))

    def test_trapezoid_tr(self):
        self.assertEqual(task4_1.kf_trapezoid(linear, a, b), linear_int(a, b))

    def test_simpson_tr(self):
        self.assertEqual(task4_1.kf_simpson(square, a, b), square_int(a, b))

    def test_38_tr(self):
        self.assertEqual(task4_1.kf_3_8(cube, a, b), cube_int(a, b))


if __name__ == '__main__':
    unittest.main()
