import unittest

from algorithms.fibonacci_recursion import fibonacci_recursive, fibonacci_recursive_memoized


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


class TestFibonacciRecursiveMemoized(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(fibonacci_recursive_memoized(0), 0)
        self.assertEqual(fibonacci_recursive_memoized(1), 1)

    def test_known_values(self):
        self.assertEqual(fibonacci_recursive_memoized(2), 1)
        self.assertEqual(fibonacci_recursive_memoized(3), 2)
        self.assertEqual(fibonacci_recursive_memoized(4), 3)
        self.assertEqual(fibonacci_recursive_memoized(5), 5)
        self.assertEqual(fibonacci_recursive_memoized(6), 8)
        self.assertEqual(fibonacci_recursive_memoized(7), 13)

    def test_large_input(self):
        # Testing a larger value to ensure memoization improves performance
        self.assertEqual(fibonacci_recursive_memoized(30), 832040)


if __name__ == '__main__':
    unittest.main()
