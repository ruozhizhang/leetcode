'''
Two points to identify an DP problem:
	1. optimal structures
		a. clear equation between the results of original problem and subproblems
	2. overlapping subproblems
		a. the calculation of subproblem can be reused
			i. Memoization (top-down cache filling)
				1) better approach when not all the results of subproblems are needed to be
        calculated
			ii. Tabulation (bottom-up cache filling)
        2) better approach when all the results of subproblems are needed to be calculated

Backpack
n items with size A[i] (each item may also have value, etc.), one backpack of size m
	a. 0/1 knapsack -> each item can only be used once
	b. each item can be used unlimited times

1) max size to put into the backpack
2) max value to put into the backpack
3) how many ways to fill the backpack

size is one dimension of the dp array, each size needs to be fully filled

  1. There are n items, each has size A[i], and a backpack with size m, what is the biggest
      size that can be put into it?
    a. f[i][j] means whether a backpack with size j can be fully filled using first i items
    b. 0 <= i <= n, 0 <= j <= m
    c. f[i][j] = f[i - 1][j] or f[i - 1][j - A[i - 1]]
      i. if not use item i - 1, result is f[i - 1][j]
      ii. if using item i - 1, result is f[i - 1][j - A[i - 1]]
          (need to have j >= A[i - 1])
    d. return value is max(j for j in range(m + 1) if f[n][j])

  2. There are n items, each has size A[i] and value V[i], and a backpack with size m, what
      is the max value of items that can be put into it?
    a. f[i][j] means the max value that can fully fill size j using first i items
    b. 0 <= i <= n, 0 <= j <= m
    c. f[i][j] = max(f[i - 1][j], f[i - 1][j - A[i - 1]] + V[i - 1])
      i. if not use item i - 1, result is f[i - 1][j]
      ii. if using item i - 1, result is f[i - 1][j - A[i - 1]] + V[i - 1]
          (need to have j >= A[i - 1])
    d. return value is max(f[n][j] for j in range(m + 1))

  3. There are n kinds of items, each has size A[i], and a backpack with size m, how many
      number of ways are there to fill the backpack? (each item can be used unlimited times)
    a. f[i][j] means the number of ways to fully fill size j using first i items
    b. 0 <= i <= n, 0 <= j <= m
    c. f[i][j] = f[i - 1][j] + f[i][j - A[i - 1]]
        i. if not use item i - 1, result is f[i - 1][j]
        ii. if use at least 1 item i - 1, result is f[i][j - A[i - 1]]
            (if at least 1 item i - 1 is used, then the rest size is j - A[i - 1], we may still use
            item i - 1 since each item can be used more than once, so result is f[i][j - A[i - 1]])
            (need to have j >= A[i - 1])
    d. return value is f[n][m]

  4. Similar to 3), only change is that each item can only be used once
    a. f[i][j] means the number of ways to fully fill size j using first i items
    b. 0 <= i <= n, 0 <= j <= m
    c. f[i][j] = f[i - 1][j] + f[i - 1][j - A[i - 1]]
        i. if not use item i - 1, result is f[i - 1][j]
        ii. if use item i - 1, result is f[i - 1][j - A[i - 1]]
            (need to have j >= A[i - 1])
    d. return value is f[n][m]
'''
