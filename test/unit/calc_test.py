import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator, InvalidPermissions


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        self.assertEqual(-4, self.calc.add(-2, -2))
        self.assertAlmostEqual(0.3, self.calc.add(0.1, 0.2), places=7)
        self.assertEqual(100, self.calc.add(99, 1))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_subtract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.subtract(2, 2))
        self.assertEqual(4, self.calc.subtract(2, -2))
        self.assertEqual(-4, self.calc.subtract(-2, 2))
        self.assertEqual(1, self.calc.subtract(1, 0))
        self.assertEqual(-1, self.calc.subtract(0, 1))
        self.assertEqual(0, self.calc.subtract(-2, -2))
        self.assertAlmostEqual(-0.1, self.calc.subtract(0.1, 0.2), places=7)
        self.assertEqual(98, self.calc.subtract(99, 1))

    def test_subtract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.subtract, "2", 2)
        self.assertRaises(TypeError, self.calc.subtract, 2, "2")
        self.assertRaises(TypeError, self.calc.subtract, "2", "2")
        self.assertRaises(TypeError, self.calc.subtract, None, 2)
        self.assertRaises(TypeError, self.calc.subtract, 2, None)
        self.assertRaises(TypeError, self.calc.subtract, object(), 2)
        self.assertRaises(TypeError, self.calc.subtract, 2, object())

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertEqual(4, self.calc.multiply(-2, -2))
        self.assertAlmostEqual(0.06, self.calc.multiply(0.2, 0.3), places=7)
        self.assertEqual(100, self.calc.multiply(10, 10))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_fails_with_nan_parameter(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)

    @patch('app.util.validate_permissions', return_value=False, create=True)
    def test_multiply_method_fails_without_permissions(self, _validate_permissions):
        self.assertRaises(InvalidPermissions, self.calc.multiply, 2, 2)

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(-1, self.calc.divide(2, -2))
        self.assertEqual(-1, self.calc.divide(-2, 2))
        self.assertEqual(1, self.calc.divide(-2, -2))
        self.assertEqual(0.5, self.calc.divide(1, 2))
        self.assertEqual(10, self.calc.divide(100, 10))
        self.assertAlmostEqual(0.333333, self.calc.divide(1, 3), places=5)

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, 2, None)

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)
        self.assertRaises(TypeError, self.calc.divide, -5, 0)

    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(1, self.calc.power(2, 0))
        self.assertEqual(1, self.calc.power(5, 0))
        self.assertEqual(0.5, self.calc.power(2, -1))
        self.assertEqual(0.25, self.calc.power(2, -2))
        self.assertEqual(9, self.calc.power(3, 2))
        self.assertEqual(1, self.calc.power(-1, 2))
        self.assertEqual(-1, self.calc.power(-1, 3))
        self.assertEqual(100, self.calc.power(10, 2))

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())

    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.sqrt(4))
        self.assertEqual(3, self.calc.sqrt(9))
        self.assertEqual(0, self.calc.sqrt(0))
        self.assertEqual(1, self.calc.sqrt(1))
        self.assertEqual(10, self.calc.sqrt(100))
        self.assertAlmostEqual(1.414213, self.calc.sqrt(2), places=5)
        self.assertAlmostEqual(2.236067, self.calc.sqrt(5), places=5)

    def test_sqrt_method_fails_with_negative_number(self):
        self.assertRaises(ValueError, self.calc.sqrt, -1)
        self.assertRaises(ValueError, self.calc.sqrt, -4)
        self.assertRaises(ValueError, self.calc.sqrt, -100)

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "4")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        self.assertRaises(TypeError, self.calc.sqrt, object())
        self.assertRaises(TypeError, self.calc.sqrt, "string")

    def test_log10_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(2, self.calc.log10(100))
        self.assertEqual(3, self.calc.log10(1000))
        self.assertEqual(0, self.calc.log10(1))
        self.assertAlmostEqual(0.30103, self.calc.log10(2), places=5)
        self.assertAlmostEqual(-1, self.calc.log10(0.1), places=5)
        self.assertAlmostEqual(-2, self.calc.log10(0.01), places=5)

    def test_log10_method_fails_with_non_positive_number(self):
        self.assertRaises(ValueError, self.calc.log10, 0)
        self.assertRaises(ValueError, self.calc.log10, -1)
        self.assertRaises(ValueError, self.calc.log10, -10)
        self.assertRaises(ValueError, self.calc.log10, -100)

    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "10")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())
        self.assertRaises(TypeError, self.calc.log10, "string")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
