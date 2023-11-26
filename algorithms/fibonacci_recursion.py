"""
The fibonacci sequence is a sequence of numbers that start with 0 and 1. Each subsequent number is a sum of the 2 preceding
numbers. So the sequence goes:
0, 1, 1, 2, 3, 5, 8, 13 etc.
our base case will be:
fib(0) = 0
fib (1) = 1

the math formular is: fib(n) = fib(n-1) + fib(n-2)

"""


def fibonacci_recursive(n):
    """
    returns the nth number of the fib sequence
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_recursive_memoized(n, memo={0: 0, 1: 1}):
    """
    a memoized version of the fib_recursive function above. Uses a dictionary to store intermediate values
    """
    if n in memo:
        return memo[n]
    f = fibonacci_recursive_memoized(n - 1) + fibonacci_recursive_memoized(
        n - 2
    )  # compute the fib number
    memo[n] = f  # store the value in the cache
    return f  # return the value to the caller
