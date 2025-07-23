
import unittest
from calculator import calculator, is_even, safe_divide


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator(2, 3, 'add'), 5)
        self.assertEqual(calculator(-1, 1, 'add'), 0)
        self.assertEqual(calculator(0, 0, 'add'), 0)
    
    def test_subtract(self):
        self.assertEqual(calculator(5, 3, 'subtract'), 2)
        self.assertEqual(calculator(-1, -1, 'subtract'), 0)
        self.assertEqual(calculator(0, 5, 'subtract'), -5)
    
    def test_multiply(self):
        self.assertEqual(calculator(3, 4, 'multiply'), 12)
        self.assertEqual(calculator(-2, 5, 'multiply'), -10)
        self.assertEqual(calculator(0, 5, 'multiply'), 0)
    
    def test_divide(self):
        self.assertEqual(calculator(10, 2, 'divide'), 5)
        self.assertEqual(calculator(-9, 3, 'divide'), -3)
        self.assertAlmostEqual(calculator(1, 3, 'divide'), 0.333333, places=6)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator(5, 0, 'divide')
    
    def test_unknown_operation(self):
        with self.assertRaises(ValueError):
            calculator(2, 3, 'modulus')


class TestIsEven(unittest.TestCase):
    def test_is_even(self):
        test_cases = [
            (0, True),
            (2, True),
            (-4, True),
            (1, False),
            (-3, False),
            (1000000, True),
            (1000001, False)
        ]
        
        for num, expected in test_cases:
            with self.subTest(num=num):
                self.assertEqual(is_even(num), expected)


class TestSafeDivide(unittest.TestCase):
    def test_safe_divide_normal(self):
        self.assertEqual(safe_divide(10, 2), 5)
        self.assertEqual(safe_divide(-9, 3), -3)
        self.assertAlmostEqual(safe_divide(1, 3), 0.333333, places=6)
    
    def test_safe_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            safe_divide(5, 0)
        
        with self.assertRaises(ZeroDivisionError):
            safe_divide(0, 0)


if __name__ == '__main__':
    unittest.main()