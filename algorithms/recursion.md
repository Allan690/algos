# Recursion

- Recursion is a concept in mathematics and computer science where a function calls itself directly or indirectly.

- Recursion solves a problem by breaking it down into smaller, more manageable sub-problems of the same type as the
original problem.

- A recursive function solves a problem by calling itself until it reaches a base case or termination condition.

- Should be used carefully as it can lead to issues like :

1. Stack overflow where the call stack of the function grows too large.
2. Infinite recursion - where the function never reaches the base case.

## Example

Consider the calculation of a factorial. The calculation of a factorial of a number `n`, denoted as `n!` is the product
of all positive integers less than or equal to n. Mathematically it can be defined as follows:

```math
n! = n * (n-1)! for n > 0
0! = 1 as base case
```

```python3
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
```

To find `n!` the function calls itself to find `(n-1)` until it reaches the base case of `0!`.

## Uses

- Tree traversal algorithms
- Implementing algorithms like quicksort and merge sort
