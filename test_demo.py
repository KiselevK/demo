import unittest
from demo import calculate


class TestCalculate(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(3, '+', 5), 8)

    def test_subtraction(self):
        self.assertEqual(calculate(9, '-', 4), 5)

    def test_multiplication(self):
        self.assertEqual(calculate(7, '*', 3), 21)

    def test_division(self):
        self.assertEqual(calculate(10, '/', 2), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(5, '/', 0)

    def test_unknown_operator(self):
        with self.assertRaises(ValueError):
            calculate(5, '^', 2)

    def test_float_addition(self):
        self.assertAlmostEqual(calculate(1.5, '+', 2.5), 4.0)

    def test_negative_numbers(self):
        self.assertEqual(calculate(-3, '+', -7), -10)


if __name__ == '__main__':
    unittest.main()
