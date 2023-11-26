def factorial_naive(n):
    """
    computes the factorial of a number n
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("factorial only works with valid positive integers")
    if n == 0:
        return 1
    return n * factorial_naive(n - 1)


def factorial_memoized(n, memo={0: 1}):
    if not isinstance(n, int) or n < 0:
        raise ValueError("factorial only works with valid positive integers")
    if n in memo:
        return memo[n]
    memo[n] = n * factorial_memoized(n - 1, memo)
    return memo[n]
