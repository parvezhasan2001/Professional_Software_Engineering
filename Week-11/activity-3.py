#Week-11
#Activity-3

import unittest
import doctest

def add(a, b):
    return a + b
def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def modulus(a, b):
    return a % b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(-1, 1), -2)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-6, -3), 2)
        self.assertEqual(divide(-6, 3), -2)
        with self.assertRaises(ValueError):
            divide(1, 0)
    def test_modulus(self):
        self.assertEqual(modulus(5, 3), 2)
        self.assertEqual(modulus(5, -3), -1)
        self.assertEqual(modulus(-5, 3), 1)
        self.assertEqual(modulus(-5, -3), -2)
        
if __name__ == "__main__":
    unittest.main()
    doctest.testmod()