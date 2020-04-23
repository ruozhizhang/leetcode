'''
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle
in the matrix such that its sum is no larger than k.

Example:
Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
'''

import bisect
class Solution:
    def maxSumSubmatrix(self, A: List[List[int]], k: int) -> int:
        m, n = len(A), len(A[0])
        rowSum = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                rowSum[i][j] = A[i][j] + (rowSum[i][j - 1] if j > 0 else 0)

        res = float('-inf')
        for i in range(n):
            for j in range(i, n):
                preSums = [0]
                preSum = 0
                for r in range(m):
                    preSum += rowSum[r][j] - (rowSum[r][i - 1] if i > 0 else 0)
                    target = preSum - k
                    index = bisect.bisect_left(preSums, target)
                    if index < len(preSums):
                        res = max(res, preSum - preSums[index])
                    bisect.insort(preSums, preSum)
        return res
