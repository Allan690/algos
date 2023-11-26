import unittest
from algorithms.factorial import factorial_memoized, factorial_naive


class TestFactorialFunctions(unittest.TestCase):

    def test_basic_functionality(self):
        for func in [factorial_naive, factorial_memoized]:
            self.assertEqual(func(5), 120)
            self.assertEqual(func(1), 1)
            self.assertEqual(func(3), 6)

    def test_edge_case_zero(self):
        for func in [factorial_naive, factorial_memoized]:
            self.assertEqual(func(0), 1)

    def test_negative_input(self):
        for func in [factorial_naive, factorial_memoized]:
            with self.assertRaises(ValueError):
                func(-1)

    def test_non_integer_input(self):
        for func in [factorial_naive, factorial_memoized]:
            with self.assertRaises(ValueError):
                func(3.5)

    def test_memoization(self):
        memo = {0:1}
        factorial_memoized(5, memo)
        self.assertTrue(4 in memo and 3 in memo and 2 in memo and 1 in memo)
