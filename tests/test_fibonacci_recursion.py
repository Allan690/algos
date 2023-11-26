import timeit
import unittest

from algorithms.fibonacci_recursion import fibonacci_bottom_up_dp, fibonacci_recursive, fibonacci_recursive_memoized


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


class TestFibonacciBottomUpDP(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(fibonacci_bottom_up_dp(0), 0)
        self.assertEqual(fibonacci_bottom_up_dp(1), 1)

    def test_known_values(self):
        self.assertEqual(fibonacci_bottom_up_dp(2), 1)
        self.assertEqual(fibonacci_bottom_up_dp(3), 2)
        self.assertEqual(fibonacci_bottom_up_dp(4), 3)
        self.assertEqual(fibonacci_bottom_up_dp(5), 5)
        self.assertEqual(fibonacci_bottom_up_dp(6), 8)
        self.assertEqual(fibonacci_bottom_up_dp(7), 13)

    def test_large_input(self):
        self.assertEqual(fibonacci_bottom_up_dp(30), 832040)

    def test_perf(self):
        test_values = [10, 20, 30, 40, 50]

        # Measure performance
        for n in test_values:
            recursive_time = timeit.timeit(lambda: fibonacci_recursive_memoized(n), number=1000)
            bottom_up_time = timeit.timeit(lambda: fibonacci_bottom_up_dp(n), number=1000)

            print(f"n={n}:")
            print(f" Recursive Memoized: {recursive_time:.6f} seconds")
            print(f" Bottom-Up DP: {bottom_up_time:.6f} seconds")

if __name__ == '__main__':
    unittest.main()
