import unittest

from algorithms.fibonacci_recursion import fibonacci_recursive


class TestFibonacciRecursive(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)

    def test_known_values(self):
        self.assertEqual(fibonacci_recursive(2), 1)
        self.assertEqual(fibonacci_recursive(3), 2)
        self.assertEqual(fibonacci_recursive(4), 3)
        self.assertEqual(fibonacci_recursive(5), 5)
        self.assertEqual(fibonacci_recursive(6), 8)
        self.assertEqual(fibonacci_recursive(7), 13)

if __name__ == '__main__':
    unittest.main()
