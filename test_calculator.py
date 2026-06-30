import unittest

from calculator import add, divide, multiply, power, subtract


class TestAdd(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_floats(self):
        self.assertAlmostEqual(add(2.5, 0.5), 3.0)


class TestSubtract(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(subtract(5, 1), 4)

    def test_negative_result(self):
        self.assertEqual(subtract(1, 5), -4)

    def test_zero(self):
        self.assertEqual(subtract(5, 5), 0)


class TestMultiply(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(multiply(4, 6), 24)

    def test_by_zero(self):
        self.assertEqual(multiply(4, 0), 0)

    def test_negative(self):
        self.assertEqual(multiply(-4, 6), -24)


class TestDivide(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(divide(10, 2), 5)

    def test_non_integer_result(self):
        self.assertAlmostEqual(divide(1, 3), 1 / 3)

    def test_negative(self):
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_zero_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            divide(0, 0)

    def test_zero_dividend(self):
        self.assertEqual(divide(0, 5), 0)


class TestPower(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(power(2, 3), 8)

    def test_exponent_zero(self):
        self.assertEqual(power(5, 0), 1)

    def test_negative_exponent(self):
        self.assertAlmostEqual(power(2, -2), 0.25)

    def test_negative_base(self):
        self.assertEqual(power(-2, 3), -8)

    def test_fractional_exponent(self):
        self.assertAlmostEqual(power(4, 0.5), 2.0)

    def test_zero_base_positive_exponent(self):
        self.assertEqual(power(0, 5), 0)

    def test_zero_base_negative_exponent_raises_value_error(self):
        with self.assertRaises(ValueError):
            power(0, -1)


if __name__ == "__main__":
    unittest.main()
