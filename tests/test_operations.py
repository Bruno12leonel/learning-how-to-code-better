"""
Unit tests for the calculator.operations module.

Best practices demonstrated here:
- Each test class groups related tests for a single function.
- Test method names describe the specific scenario being tested.
- Both normal cases and edge cases are covered.
- Assertions use the most specific method available (e.g. assertAlmostEqual
  for floats) so failures produce clear messages.
- Exceptions are tested with assertRaises to confirm error handling works.
"""

import unittest

from calculator.operations import add, divide, multiply, subtract


class TestAdd(unittest.TestCase):
    """Tests for the add() function."""

    def test_add_two_positive_numbers(self):
        self.assertEqual(add(3, 4), 7)

    def test_add_positive_and_negative_number(self):
        self.assertEqual(add(-1, 1), 0)

    def test_add_two_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_with_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_add_float_numbers(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3, places=5)


class TestSubtract(unittest.TestCase):
    """Tests for the subtract() function."""

    def test_subtract_smaller_from_larger(self):
        self.assertEqual(subtract(10, 3), 7)

    def test_subtract_larger_from_smaller_gives_negative(self):
        self.assertEqual(subtract(0, 5), -5)

    def test_subtract_equal_numbers_gives_zero(self):
        self.assertEqual(subtract(7, 7), 0)

    def test_subtract_negative_number(self):
        self.assertEqual(subtract(5, -3), 8)


class TestMultiply(unittest.TestCase):
    """Tests for the multiply() function."""

    def test_multiply_two_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_positive_and_negative_gives_negative(self):
        self.assertEqual(multiply(-2, 5), -10)

    def test_multiply_by_zero_gives_zero(self):
        self.assertEqual(multiply(99, 0), 0)

    def test_multiply_two_negatives_gives_positive(self):
        self.assertEqual(multiply(-3, -4), 12)


class TestDivide(unittest.TestCase):
    """Tests for the divide() function."""

    def test_divide_even_numbers(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_produces_decimal_result(self):
        self.assertAlmostEqual(divide(7, 2), 3.5, places=5)

    def test_divide_by_one_returns_dividend(self):
        self.assertEqual(divide(42, 1), 42.0)

    def test_divide_negative_dividend(self):
        self.assertEqual(divide(-10, 2), -5.0)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_divide_by_zero_error_message(self):
        with self.assertRaises(ValueError) as context:
            divide(5, 0)
        self.assertIn("zero", str(context.exception).lower())


if __name__ == "__main__":
    unittest.main()
