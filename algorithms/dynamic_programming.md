# Dynamic Programming

- Is a method for solving problems by breaking them down into simpler sub-problems. DP = Recursion + memoization.
- It is applicable to problems exhibiting the properties of overlapping subproblems and optimal substructure.

1. Overlapping subproblems
 This property means that the problem can be broken down into subproblems which are reused several times. For example, in the Fibonacci sequence, to calculate fib(5), you need fib(4) and fib(3), and to calculate fib(4), you need fib(3) and fib(2). Here, the subproblem fib(3) is used to compute both fib(4) and fib(5). In a naive recursive approach, the same computations are repeated multiple times, leading to inefficiency.

2. Optimal substructure
A problem exhibits optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. For instance, in a shortest path problem like the one solved by Dijkstra's algorithm, the shortest path from point A to point C via point B is the combination of the shortest path from A to B and from B to C.

Dynamic programming approaches can be categorized into two main types:

`Top-Down (Memoization)`: This approach involves writing the problem as a recursive algorithm that solves the subproblems and stores the results (memoizes them) to avoid redundant work. This is like the recursive approach with a cache.

`Bottom-Up (Tabulation)`: Here, the problem is solved by building up a table of solutions to smaller subproblems in a manner that the larger problems rely on the solutions of these smaller ones. This approach often iterates through a series of decisions, storing the results in a table.

## Uses

- Solving resource allocation problems in economics.
- Solving CS problems like text edit distance, shortest paths in graphs etc.
- Operations research
